from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView
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
    return HttpResponseRedirect(reverse('coins:coin-make-offer', kwargs={"pk": coin_id}))


class CoinMakeOfferView(DetailView):
    model = Coin
    template_name = 'coins/coin_make_offer.html'

def make_offer(request):
    coin_to_get_id = request.POST.get('coin_to_get_id')
    coin_to_give_id = request.POST.get('coin_to_give_id')
    if coin_to_get_id and coin_to_give_id:        
        coin_to_get = Coin.objects.get(id=coin_to_get_id)
        coin_to_give = Coin.objects.get(id=coin_to_give_id)
        new_offer = Offer(
            coin_to_get=coin_to_get,
            coin_to_give=coin_to_give,
            author = coin_to_give.owner,
            responder=coin_to_get.owner,
            )
        new_offer.save()

       
    return HttpResponseRedirect(reverse('coins:index'))

# class OfferByUserListView(ListView):
#     model = Offer
#     template_name = 'coins/ofers_by_user.html'
    
def offers_by_user(request):
    context = {
        'object_list': Offer.objects.filter(responder=request.user, status='c')
    }
    return render(request, template_name="coins/ofers_by_user.html", context=context)

def remove_offer(request, pk):
    offer = Offer.objects.get(id=pk)
    offer.delete()
    return HttpResponseRedirect(reverse('coins:index'))

def accept_offer(request, pk):
    offer = Offer.objects.get(id=pk)
    coin_to_get = offer.coin_to_get
    coin_to_give = offer.coin_to_give
    user_1 = coin_to_get.owner
    user_2 = coin_to_give.owner
    coin_to_get.owner = user_2
    coin_to_get.save()
    coin_to_give.owner = user_1
    coin_to_give.save()
    offer.status = 'd'
    offer.save()
    return HttpResponseRedirect(reverse('coins:index'))
