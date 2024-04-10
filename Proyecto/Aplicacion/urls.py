# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('juguetes/', views.juguetes, name='juguetes'),
    path('ropa/', views.ropa, name='ropa'),
]