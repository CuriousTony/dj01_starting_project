from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Главная'),
    path('new/', views.new, name='Контент'),
    path('about/', views.about, name='О компании'),
    path('contacts/', views.contacts, name='Контакты')
]
