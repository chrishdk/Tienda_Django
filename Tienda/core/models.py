from django.db import models
from django.db.models.query import FlatValuesListIterable

# Create your models here.


#  crear modelo para categoria
class categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria

#creando modelos de los productos

class Productos(models.Model):
    codProducto = models.CharField(max_length=6, primary_key=True,verbose_name="Codigo producto")
    nomProducto = models.CharField(max_length=15, blank=False, null=False, verbose_name="Nombre producto")
    imagen = models.ImageField(upload_to="images/",default="sinfoto.png", null=False, blank=False, verbose_name="Imagen producto")
    precioProducto = models.IntegerField(max_length=8, null=False,blank=False, verbose_name="Precio Producto" )
    categoria = models.ForeignKey(categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.codProducto
