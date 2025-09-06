from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/add/', views.client_create, name='client_create'),
    path('trainers/', views.trainer_list, name='trainer_list'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
]
