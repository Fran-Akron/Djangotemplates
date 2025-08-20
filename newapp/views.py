from django.shortcuts import render

# Create your views here.

# newapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'newapp/home.html')