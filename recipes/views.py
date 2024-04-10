from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, "recipes/home.html", context=context)

def sobre(request):
    return HttpResponse("SOBRE")

def contato(request):
    return HttpResponse("CONTATO")
