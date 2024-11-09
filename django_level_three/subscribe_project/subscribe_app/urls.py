from django.urls import path, include 
from subscribe_app import views

urlpatterns = [
    path('', views.customers, name='customers'),
]