from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def hardware(request):
    return render(request, "core/Hardware.html")

    
def notebook(request):
    return render(request, "core/Notebooks.html")

def contacto(request):
    return render(request, "core/Contacto.html")

def acercade(request):
    return render(request, "core/AcercaDe.html")

def iniciosesion(request):
    return render(request, "core/InicioSesion.html")

def registro(request):
    return render(request, "core/Registro.html")

def carrito(request):
    return render(request, "core/Carrito.html")

def terminocondiciones(request):
    return render(request, "core/TerminoCondiciones.html")

def politicaprivacidad(request):
    return render(request, "core/PoliticaPrivacidad.html")