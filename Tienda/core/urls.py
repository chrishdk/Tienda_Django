from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,hardware


urlpatterns = [
    path('', home, name="home"),
    path('home.html', home, name="home"),
    path('Hardware.html', hardware, name="hardware"),
]