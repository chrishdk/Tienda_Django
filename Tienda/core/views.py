from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from core.models import Categoria, Persona,  Producto
from core.forms import  ValidarPersonaForm , ProductoForm, IniciarSesionForm
from django.contrib.auth import login, logout, authenticate



# Create your views here.

# Vistas de pag heredadas

def home(request):
    data = {"list": Producto.objects.all().order_by('codProducto')}
    return render(request, "core/home.html", data)

def hardware(request):
    data = {"list": Producto.objects.filter(categoria="1").order_by('codProducto')}
    return render(request, "core/Hardware.html", data)

def notebook(request):
    data = {"list": Producto.objects.filter(categoria="2").order_by('codProducto')}
    return render(request, "core/Notebooks.html", data)

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

def producto_ficha(request, id):
    producto = Producto.objects.get(codProducto=id)
    data = {"Producto":  producto}
    return render(request, "core/producto_ficha.html", data)

# Validar Usuario

def inicio_sesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}   

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(home)
                    else:
                        data["mesg"] ="cuenta o password incorrectas"
                else:
                    data["mesg"]="cuenta o password incorrectos"
    return render(request, "core/InicioSesion.html", data)
#cerrar seion
def cerrar_sesion(request):
    logout(request)
    return redirect(home)


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

#producto 1 
    Producto.objects.create(codProducto="1",
                            nomProducto='HP Omen 15-EN0002LA',
                            imagen="images/Notebook/001/001.png",
                            precioProducto="1099990",
                            precioProductoCred="1249990",
                            descFich="AMD Ryzen 7 4800H / RAM 16 GB DDR4 / Pantalla LED 15.6'' / NVIDIA GeForce RTX 2060 /"  ,
                            descFichCom="HP Omen 15-EN0002LA   /   Procesador AMD Ryzen 7 4800H (8 núcleos / 16 hilos / 2900 MHz - 4200 MHz)   /   RAM 16 GB DDR4 (3200 MHz)   /   Pantalla LED 15.6' (1920x1080) / 60 Hz   /   Batería 6 celdas (70900 mWh)   /   AlmacenamientoSSD 512GB   /   NVIDIA GeForce RTX 2060 (6 GB)   /   Dimensiones 358 x 240 x 23 mm   /   Sistema Operativo Microsoft Windows 10 Home",
                            categoria=Categoria.objects.get(idCategoria=2))

#producto 2
    Producto.objects.create(codProducto="2",
                            nomProducto='ASUS TUF Gaming F15',        
                            imagen="images/Notebook/002/002.png",      
                            precioProducto="869990"  , 
                            precioProductoCred="899990",                         
                            descFich="Notebook Asus Tuf Gaming F15 / Fortress Gray / Amd Rayzen 7 / 8 Gb Ram / Nvidia Geforce gtx 1650 ti / 512 Gb / Pantalla '15.6 " ,
                            descFichCom="Procesador AMD Ryzen 7 4800H (8 núcleos / 16 hilos / 2900 MHz - 4200 MHz)   /  RAM 8 GB DDR4 (2933 MHz)   /   Pantalla LED 15.6' (1920x1080) / 144 Hz   /   Batería 3 celdas (48000 mWh)   /   Almacenamiento SSD 512GB   /   Tarjetas de video AMD Radeon RX Vega 7 (Integrada) NVIDIA GeForce GTX 1650 Ti (4 GB) Puertos   /   Dimensiones 359 x 256 x 25 mm   /Sistema Operativo Microsoft Windows 10 Home",                  
                            categoria=Categoria.objects.get(idCategoria=2))
#producto 3
    Producto.objects.create(codProducto="3",
                            nomProducto='ASUS Chromebook C423NA-WB04',
                            imagen="images/Notebook/003/003.png",
                            precioProducto="209990", precioProductoCred="209990",
                            descFich="Asus chromebook C423NA-WB04 / Intel Celeron N3350 / Memoria RAM: 4 GB / Disco Duro: 64 GB / Sistema operativo: Chrome OS / Pantalla: '14 (1366x768)"  ,
                            descFichCom="Asus chromebook C423NA-WB04   /   Procesador Intel Celeron N3350 (2 núcleos / 2 hilos / 1100 MHz - 2400 MHz)   /   RAM 4 GB LPDDR4 (2400 MHz)   /   Pantalla LED 14.0' (1366x768) / 60 Hz   /   Batería 3 celdas (38000 mWh)   /   Tarjetas de video Intel HD Graphics 500 (Integrada)   /   Dimensiones 323 x 229 x 16 mm   /   Sistema Operativo Google Chrome OS",
                            categoria=Categoria.objects.get(idCategoria=2))
#producto 4
    Producto.objects.create(codProducto="4",
                            nomProducto='Intel Core i7-11700F',
                            imagen="images/Procesador/001/001.png",
                            precioProducto="319900",
                            precioProductoCred="319900",
                            descFich="Intel core i7 de 11ma Generación / 8 núcleos / Frecuencia del procesador 2,5 GHz / 64 bits"  ,
                            descFichCom="Intel Core i7 de 11ma Generación   /   Número de núcleos de procesador: 8   /   Socket de procesador: LGA1200-V1   /   Fabricante de procesador: Intel   /    Frecuencia del procesador 2,5 GHz   /   Número de filamentos de procesador: 16    /   Modo de procesador operativo: 64 bits",
                            categoria=Categoria.objects.get(idCategoria=1))
    #producto 5
    Producto.objects.create(codProducto="5",
                            nomProducto='GSkill Trident Z',
                            imagen="images/ram/001/001.png",
                            imagen2="images/ram/001/001c.png",
                            precioProducto="59990"  ,
                            precioProductoCred="59990",
                            descFich="GSkill Trident Z / Memoria interna 8 GB / Velocidad de memoria 2400 MHz / Retroiluminación RGB"  ,
                            descFichCom="GSkill Trident Z   / Memoria interna 8GB   /   Tipo de memoria interna: DDR4   /   Velocidad de memoria del reloj: 2400 MHz   /   Intel® Extreme Memory Profile (XMP): Si   /   Voltaje de memoria: 1.35 V   /   Tipo de enfriamiento: Disipador térmico   /   Retroiluminación: Si   /   Color de luz de fondo: Rojo/Verde/Azul",
                            categoria=Categoria.objects.get(idCategoria=1))
    #producto 6
    Producto.objects.create(codProducto="6",
                            nomProducto='MSI GeForce GTX 1660 GAMING X 6G',
                            imagen="images/Video/001/001.png",
                            precioProducto="289990", precioProductoCred="289990",
                            descFich="NVIDIA GTX 1660 / Resolución 7680 x 4320 pixeles / Capacidad gráfica 6 GB / Ancho de datos 192 bits / interfaz PCI Express x16 3.0"  ,
                            descFichCom="Familia de procesadores gráficos NVIDIA   /   Procesador gráfico GeForce GTX 1660   /   máxima resolucion 7680x4320   /   Máximas pantallas por tarjeta de video: 4   /   Capacidad de memoria gráfica: 6 GB   /   Tipo de interfaz:  PCI Express x16 3.0   /   velocidad de transferencia de datos 8 Gbit/s   /   Ancho de datos: 192 bits",
                            categoria=Categoria.objects.get(idCategoria=1))
    return redirect(producto, action='ins', id = '-1')
