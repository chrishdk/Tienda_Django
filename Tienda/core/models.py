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
    descFich = models.CharField(max_length=200, null=True, blank=False, verbose_name="Descripcion Ficha")
    descFichCom = models.CharField(max_length=500, null=True, blank=False, verbose_name="Descripcion Ficha Completa")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.codProducto

class Persona(models.Model):
    cuenta = models.CharField(max_length=50, primary_key=True, verbose_name="Cuenta")
    rut = models.CharField(max_length=80, blank=False, null=False, verbose_name="Rut")
    nombre = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre")
    password = models.CharField(max_length=80, blank=False, null=False, verbose_name="Contraseña")

    def __str__(self):
        return f"{self.nombre} ({self.cuenta})"
