from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,hardware


urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('hardware', hardware, name="hardware"),
]