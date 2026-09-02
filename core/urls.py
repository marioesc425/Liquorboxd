from django.urls import path
from . import views

urlpatterns = [
    ##At true root
    path('', views.home, name='home'),
]