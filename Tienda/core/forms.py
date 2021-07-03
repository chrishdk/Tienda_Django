from django import forms
from django.forms import ModelForm, fields
from .models import  Persona, Producto
 
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

class ValidarPersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['cuenta', 'password']