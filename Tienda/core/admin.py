from django.contrib import admin
from .models import Categoria, Persona, Producto 
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Persona)
