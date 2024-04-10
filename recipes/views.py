from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {"name": "felipe"}
    return render(request, "recipes/home.html", context=context, status=201)

def sobre(request):
    return render(request, "contato.html", context={})

def contato(request):
    return HttpResponse("CONTATO")
