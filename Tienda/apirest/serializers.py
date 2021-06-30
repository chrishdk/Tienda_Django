from rest_framework import fields, serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codProducto', 'nomProducto', 'imagen', 'precioProducto', 'categoria']