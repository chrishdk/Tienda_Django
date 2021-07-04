from django import forms
from django.forms import ModelForm, fields, Form, models
from .models import  Persona, Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class IniciarSesionForm(Form):
    username= forms.CharField(widget=forms.TextInput(), label="Usuario")
    password= forms.CharField(widget=forms.PasswordInput(), label="contraseña")
    class Meta:
        fields = ['username', 'password']


class RegistroForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels ={
            'username': 'Nombre de usuario ',
            'first_name': 'Nombre',
            'last_name ': 'Apellido',
            'email': "Correo",
            
        }