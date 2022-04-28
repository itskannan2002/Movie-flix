from django.urls import path
from . import views
urlpatterns=[
    path('', views.mark, name='mark'),
    path('add_mark/<int:product_id>/', views.add_mark, name='add_mark'),
    path('remove_mark/<int:product_id>/', views.remove_mark, name='remove_mark'),
    path('remove_mark/<int:product_id>/<int:mark_item_id>/', views.remove_mark, name='remove_mark'),
    path('remove_mark/<int:product_id>/<int:mark_item_id>/', views.remove_mark, name='remove_mark'),

]