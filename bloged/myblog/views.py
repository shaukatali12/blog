from django.shortcuts import rendirect  
from django.shortcuts import render


# Create your views here.
def home(request):
    return rendirect('home.html')

def card(request):
    return rendirect('card.html')

def web(request):
    return rendirect('web.html')