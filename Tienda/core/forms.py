from django import forms
from django.forms import ModelForm, fields
from .models import Producto, Usuario
 
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codProducto', 'nomProducto', 'imagen', 'precioProducto', 'categoria']

class ValidarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['cuentaUsuario', 'passUsuario']