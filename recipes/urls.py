from django.urls import path
from .views import contato, sobre, home


urlpatterns = [
    path("", home, name="home"),
]
