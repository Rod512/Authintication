from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.login, name='login'),
    path('home_page/', views.homepage, name = 'homepage')
]
