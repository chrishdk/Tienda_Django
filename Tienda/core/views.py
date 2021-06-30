from django.shortcuts import redirect, render
from core.models import Categoria, Usuario,  Producto
from core.forms import  ValidarUsuarioForm , ProductoForm



# Create your views here.

# Vistas de pag heredadas

def home(request):
    data = {"list": Producto.objects.all().order_by('codProducto')}
    return render(request, "core/home.html", data)

def hardware(request):
    return render(request, "core/Hardware.html")

    
def notebook(request):
    data = {"list": Producto.objects.all().order_by('codProducto')}
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

# Vistas nuevas


def producto_tienda(request):
    data = {"list": Producto.objects.all().order_by('codProducto')}
    return render(request, "core/producto_tienda.html", data)
def producto_ficha(request, id):
    producto = Producto.objects.get(codProducto=id)
    data = {"Producto":  producto}
    return render(request, "core/producto_ficha.html", data)

def tienda(request):
    data = {"list": Producto.objects.all().order_by('codProducto')}
    return render(request, "core/tienda.html", data)
    
# Validar Usuario

def validar_persona(request):
    data = {"mesg": "", "form": ValidarUsuarioForm, "persona": ""}

    if request.method == "POST":
        form = ValidarUsuarioForm(request.POST)
        if form.is_valid:
            try:
                cuentaUsuario = request.POST.get('cuentaUsuario')
                passUsuario = request.POST.get('passUsuario')
                objeto = Usuario.objects.get(cuentaUsuario=cuentaUsuario, passUsuario=passUsuario)
                data["mesg"] = "¡La cuenta y la password son correctos!"
                data["persona"] = Usuario.objects.get(cuentaUsuario=cuentaUsuario)
                return render(request, "core/home.html", data)
            except:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "core/ValidarPersona.html", data)

# Agregar producto

def producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡ El Producto fue agregado correctamente !"
                except:
                    data["mesg"] = "¡ No se puede agregar dos productos con el mismo id !"

# Update producto

    elif action == 'upd':
        objeto = Producto.objects.get(codProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)

# Eliminar producto        
    elif action == 'del':
            try:
                Producto.objects.get(codProducto=id).delete()
                data["mesg"] = "¡El producto fue eliminado correctamente!"
                return redirect(producto, action='ins', id = '-1')
            except:
                data["mesg"] = "¡El producto ya estaba no existe!"

    data["list"] = Producto.objects.all().order_by('codProducto')
    return render(request, "core/Producto.html", data)


def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(codProducto="1", nomProducto='HP Omen 15-EN0002LA',         imagen="images/Notebook/001/001.png",      precioProducto="1099990", precioProductoCred="1249990",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="2", nomProducto='Saleen',        imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="3", nomProducto='Shelby',        imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="4", nomProducto='Mercedes-Benz', imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    
    Producto.objects.create(codProducto="5", nomProducto='Ford',          imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="6", nomProducto='Ford',          imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="7", nomProducto='Rolls-Royce',   imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="8", nomProducto='Mustang',       imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(codProducto="9", nomProducto='Mercedes-Benz', imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(codProducto="10", nomProducto='Silver Plus',   imagen="images/Sin título.jpg",      precioProducto="100000",    categoria=Categoria.objects.get(idCategoria=1))
    return redirect(producto, action='ins', id = '-1')
