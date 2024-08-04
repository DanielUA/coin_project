from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import logout, login, authenticate

from .models import *

class IndexView(TemplateView):
    template_name = 'coins/index.html'
    extra_context = {
        "coin_list": Coin.objects.order_by('?'),
        "continent_list": Continent.objects.order_by("name"),
    }
    
class CoinDetailView(DetailView):
    model = Coin

    

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request, user) 
    return HttpResponseRedirect(reverse('coins:index'))

       
def signout(request):
    # add_countries()
    logout(request) 
    return HttpResponseRedirect(reverse('coins:index'))


def offer_detail(request):
    coin_id = request.POST.get('coin_id')
    return HttpResponseRedirect(reverse('coins:index'))

