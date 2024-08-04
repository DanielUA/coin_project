from django.urls import path
from . import views


app_name = 'coins'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sign/out/', views.signout, name='sign-out'),
    path('sign/in/', views.signin, name='sign-in'),
    path('coin/<int:pk>/', views.CoinDetailView.as_view(), name='coin-detail'),
    path('offer/detail/', views.offer_detail, name='offer-detail'),
]