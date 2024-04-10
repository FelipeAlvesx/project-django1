from django.urls import path
from .views import contato, sobre, home


urlpatterns = [
    path("", home, name="home"),
    path("contato/", contato, name="contato"),
    path("sobre/", sobre, name="sobre"),
]
