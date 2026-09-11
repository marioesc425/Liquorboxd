from django.urls import path
from . import views

urlpatterns = [
    path('', views.spirit_list, name='spirit_list'),
    path('<int:pk>/', views.spirit_detail, name='spirit_detail'),
    path('<int:pk>/add_review/', views.add_review, name='add_review'),
    path('api/spirits/', views.spirit_list_api, name='spirit_list_api'),
    path('api/spirits/<int:pk>/', views.spirit_detail_api, name='spirit_detail_api')
]