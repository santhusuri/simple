from django.urls import path
from . import views

urlpatterns = [
    path('', views.malicious_home, name='malicious_home'),
    path('redirect/', views.open_redirect, name='open_redirect'),
]