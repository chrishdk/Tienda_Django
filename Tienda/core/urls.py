from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,hardware, notebook, contacto, acercade, iniciosesion, registro, carrito


urlpatterns = [
    path('', home, name="home"),
    path('hardware', hardware, name="hardware"),
    path('Notebook', notebook, name="notebook"),
    path('Contacto', contacto, name="contacto"),
    path('AcercaDe', acercade, name="acercade"),
    path('InicioSesion', iniciosesion, name="iniciosesion"),
    path('Registro', registro, name="registro"),
    path('Carrito', carrito, name="carrito"),
]