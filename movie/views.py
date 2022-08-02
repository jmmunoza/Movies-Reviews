from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'Juan Manuel'})

def about(request):
    return render(request, 'about.html')