# views.py
from django.shortcuts import render

def ropa(request):
    return render(request, 'ropa.html')

def juguetes(request):
    return render(request, 'juguetes.html')