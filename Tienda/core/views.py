from django.shortcuts import redirect, render
from core.models import Categoria, Usuario,  Producto
from core.forms import  ValidarUsuarioForm , ProductoForm



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

#producto 1 
    Producto.objects.create(codProducto="1",
                            nomProducto='HP Omen 15-EN0002LA',
                            imagen="images/Notebook/001/001.png",
                            precioProducto="1099990",
                            precioProductoCred="1249990",
                            descFich="AMD Ryzen 7 4800H / RAM 16 GB DDR4 / Pantalla LED 15.6'' / NVIDIA GeForce RTX 2060 /"  ,
                            descFichCom="lala",
                            categoria=Categoria.objects.get(idCategoria=2))

#producto 2
    Producto.objects.create(codProducto="2",
                            nomProducto='ASUS TUF Gaming F15',        
                            imagen="images/Notebook/002/002.png",      
                            precioProducto="869990"  , 
                            precioProductoCred="899990",                         
                            descFich="Notebook Asus Tuf Gaming F15 / Fortress Gray / Amd Rayzen 7 / 8 Gb Ram / Nvidia Geforce gtx 1650 ti / 512 Gb / Pantalla '15.6 " ,
                            descFichCom="lala",                  
                            categoria=Categoria.objects.get(idCategoria=2))
#producto 3
    Producto.objects.create(codProducto="3",
                            nomProducto='ASUS Chromebook C423NA-WB04',
                            imagen="images/Notebook/003/003.png",
                            precioProducto="209990", precioProductoCred="209990",
                            descFich="Intel Celeron N3350 / Memoria RAM: 4 GB / Disco Duro: 64 GB / Sistema operativo: Chrome OS / Pantalla: '14 (1366x768)"  ,
                            descFichCom="lala",
                            categoria=Categoria.objects.get(idCategoria=2))
#producto 4
    Producto.objects.create(codProducto="4",
                            nomProducto='Intel Core i7-11700F',
                            imagen="images/Procesador/001/001.png",
                            precioProducto="319900",
                            precioProductoCred="319900",
                            descFich="Aumente su productividad, juegos y experiencias de creación de contenido instalando el procesador Intel Core i7-11700F de ocho núcleos LGA 1200 a 2.5 GHz en su sistema informático."  ,
                            descFichCom="lala",
                            categoria=Categoria.objects.get(idCategoria=1))
    #producto 5
    Producto.objects.create(codProducto="5",
                            nomProducto='GSkill Trident Z',
                            imagen="images/ram/001/001.png",
                            imagen2="images/ram/001/001c.png",
                            precioProducto="59990"  ,
                            precioProductoCred="59990",
                            descFich="Revela tus colores interiores \n ¡Crea una PC única con el kit de memoria Trident Z RGB! Lo mejor de tener capacidades RGB es la facultad de elegir los colores que desee. Ya sea blanco en un día o verde en el siguiente, puede estar seguro de que estos módulos se verán actuales y modernos en cualquier compilación."  ,
                            descFichCom="lala",
                            categoria=Categoria.objects.get(idCategoria=1))
    #producto 6
    Producto.objects.create(codProducto="6",
                            nomProducto='MSI GeForce GTX 1660 GAMING X 6G',
                            imagen="images/Video/001/001.png",
                            precioProducto="289990", precioProductoCred="289990",
                            descFich="Prepárate para jugar los últimos juegos con GeForce GTX 1660 Ti, con un desempeño que rivaliza a las GeForce GTX 1070."  ,
                            descFichCom="lala",
                            categoria=Categoria.objects.get(idCategoria=1))
    
    return redirect(producto, action='ins', id = '-1')
