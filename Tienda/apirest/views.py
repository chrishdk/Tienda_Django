#from Tienda.core.forms import RegistroForm
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import DataAndFiles, JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class producto_create(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class producto_update(APIView):
    def put(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated),)
def producto_read(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(Producto, codProducto=id)
        serializer = ProductoSerializer(objeto)
        return Response(serializer.data)

@api_view(['GET'])
def producto_read_all(request):
    if request.method == 'GET':
        list = Producto.objects.all()
        serializer = ProductoSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def producto_delete(request, id):
    if request.method == 'DELETE':
        try:
            Producto.objects.get(codProducto=id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login (request):
    data = JSONParser().parse(request)
    username= data['username']
    password= data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response ("Usuario no valido")
    password_valida = check_password(password, user.password)
    if not password_valida:
       return Response("contraseña incorrecta")
    token, created = Token.objects.get_or_create(user=user)
    print(f"este es el token creado: '{token.key}'" )
    return Response(token.key)

