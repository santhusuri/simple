from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo_home, name='project1_home'),
    path('login/', views.demo_login, name='project1_login'),
]