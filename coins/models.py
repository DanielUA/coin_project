from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    user_pic = models.ImageField(blank=True, upload_to='coins/user_pic/')

    def has_offers_under_consideration(self):
        offers = Offer.objects.filter(responder=self.user, status='c')
        return offers.exists()
    
class Continent(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Continent"
        verbose_name_plural = "Continents"

    def __str__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="countries")

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
    
safety_choices = [('v', 'v'), ('vf', 'vf'), ('f', 'f'), ('xf', 'xf')]
material_choices = [
    ("gold", "au"),
    ("silver", "ag"),
    ("platinum", "pt"),
    ("palladium", "pd"),
    ("copper", "cu"),
    ("nickel", "ni"),
    ("zinc", "zn"),
    ("tin", "sn"),
    ("bronze", "bronze"),        # bronze is a metal alloy, not a pure element
    ("brass", "brass"),         # brass is also a metal alloy
    ("cupronickel", "cupronickel"),   # cupronickel is a metal alloy
    ("aluminum", "al"),
    ("iron", "fe"),
    ("lead", "pb"),
    ("magnesium", "mg"),
    ("magnetic metals", "magnetic metals"), # general category, not a specific metal
    ("titanium", "ti")
]



class Coin(models.Model):
    img_front = models.ImageField(upload_to='products_image', blank=True)
    img_back = models.ImageField(upload_to='products_image', blank=True)
    img_add_1 = models.ImageField(upload_to='products_image', blank=True)
    img_add_2 = models.ImageField(upload_to='products_image', blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='coins')  # Reference to Country
    denomination = models.CharField(max_length=150)  # Denomination
    year = models.IntegerField()  # Year
    material = models.CharField(max_length=15, blank=True, choices=material_choices)  # Material
    safety = models.CharField(max_length=2, blank=True, choices=safety_choices)  # Optional field for admin use
    weight = models.FloatField(blank=True, null=True)  # Weight
    diameter = models.FloatField(blank=True, null=True)  # Diameter
    thickness = models.FloatField(blank=True, null=True)  # Thickness
    circulation = models.IntegerField(blank=True, null=True)  # Circulation
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coins')
    box = models.ForeignKey('Box', on_delete=models.SET_NULL, blank=True, null=True, related_name='coins')

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'

    def __str__(self):
        return f'{self.country.name} - {self.denomination} - {self.year}'   
    
class Box(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

status_choices = [('с', 'under consideration'), ('d', 'done')]

class Offer(models.Model):
    coin_to_get = models.OneToOneField(Coin, related_name='offer_get', on_delete=models.CASCADE)
    coin_to_give = models.OneToOneField(Coin, related_name='offer_give', on_delete=models.CASCADE)
    author = models.OneToOneField(User, related_name='offers_made', on_delete=models.CASCADE)
    responder = models.OneToOneField(User, related_name='offers_look', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_choices, default='c')
    created = models.DateTimeField(auto_now_add=True) 

