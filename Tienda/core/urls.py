from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,hardware, notebook, contacto, acercade, iniciosesion, registro, carrito, terminocondiciones, politicaprivacidad,poblar_bd,producto,producto_ficha,validar_persona


urlpatterns = [
    path('', home, name="home"),
    path('hardware', hardware, name="hardware"),
    path('Notebook', notebook, name="notebook"),
    path('Contacto', contacto, name="contacto"),
    path('AcercaDe', acercade, name="acercade"),
    path('InicioSesion', iniciosesion, name="iniciosesion"),
    path('Registro', registro, name="registro"),
    path('Carrito', carrito, name="carrito"),
    path('TerminoCondiciones', terminocondiciones, name="terminocondiciones"),
    path('PoliticaPrivacidad', politicaprivacidad, name="politicaprivacidad"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="producto"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('validar_persona/', validar_persona, name="validar_persona"),
]