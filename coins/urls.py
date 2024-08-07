from django.urls import path
from . import views


app_name = 'coins'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign/out/', views.signout, name='sign-out'),
    path('sign/in/', views.signin, name='sign-in'),
    path('coin/<int:pk>/', views.CoinDetailView.as_view(), name='coin-detail'),
    path('offer/detail/', views.offer_detail, name='offer-detail'),
    path('coin/<int:pk>/offer/', views.CoinMakeOfferView.as_view(), name='coin-make-offer'),
    path('make/offer/', views.make_offer, name='make-offer'),
    # path('user/offers/', views.OfferByUserListView.as_view(), name='user-offers'),
    path('user/offers/', views.offers_by_user, name='user-offers'),
    path('offer/<int:pk>/remove/', views.remove_offer, name='remove-offer'),
    path('offer/<int:pk>/accept/', views.accept_offer, name='accept-offer'),
]