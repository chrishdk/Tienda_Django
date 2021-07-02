from django.db import models
from django.db.models.query import FlatValuesListIterable

# Create your models here.


#  crear modelo para categoria
class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria

#creando modelos de los productos

class Producto(models.Model):
    codProducto = models.CharField(max_length=6, primary_key=True,verbose_name="Codigo producto")
    nomProducto = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre producto")
    imagen = models.ImageField(upload_to="images/",default="sinfoto.png", null=False, blank=False, verbose_name="Imagen producto")
    imagen2 = models.ImageField(upload_to="images/",default="sinfoto.png", null=True, blank=False, verbose_name="Imagen producto2")
    precioProducto = models.IntegerField(null=False,blank=False, verbose_name="Precio Producto" )
    precioProductoCred = models.IntegerField(null=True, blank=False, verbose_name="Precio Producto" )
    descFich = models.CharField(max_length=200, null=True, blank=False, verbose_name="descFich")
    descFichCom = models.CharField(max_length=500, null=True, blank=False, verbose_name="descFichCom")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.codProducto

class Usuario(models.Model):
    cuentaUsuario = models.CharField(max_length=20, primary_key=True,verbose_name="Cuenta")
    passUsuario = models.CharField(max_length=15, blank=False, null=False, verbose_name="Password")
    emailUsuario = models.CharField(max_length=50, blank=False, null=False, verbose_name="email")
    nomUsuario = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre")
    celUsuario = models.CharField(max_length=50, blank=False, null=False, verbose_name="Celular")
    
