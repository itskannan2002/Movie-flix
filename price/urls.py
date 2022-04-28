from django.urls import path
from . import views


urlpatterns = [
    path('', views.subplan, name='subplan'),
    path('basic/', views.basic, name='basic'),
    path('saver/', views.saver, name='saver'),
    path('premimum/', views.premimum, name='premimum'),
    path('<slug:Priceplan_slug>/', views.payment_detail, name='payment_detail'),



]
