from django import forms
from django.forms import ModelForm, fields
from .models import  Usuario, Producto
 
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codProducto',
                    'nomProducto',
                    'imagen',
                    'precioProducto',
                    'precioProductoCred',
                    'descFich',
                    'descFichCom',                    
                    'categoria'
                ]

class ValidarUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['cuentaUsuario', 'passUsuario']