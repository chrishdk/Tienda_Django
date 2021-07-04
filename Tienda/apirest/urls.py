from django.urls import path
from django.contrib import admin
from .views import producto_create, producto_read, producto_read_all, producto_update, producto_delete,login

urlpatterns = [
    path('producto_create/', producto_create.as_view(), name="producto_create"),
    path('producto_update/', producto_update.as_view(), name="producto_update"),
    path('producto_read/<id>/', producto_read, name="producto_read"),
    path('producto_read_all/', producto_read_all, name='producto_read_all'),
    path('producto_delete/<id>/', producto_delete, name="producto_delete"),
    path('login/', login, name='login')
]