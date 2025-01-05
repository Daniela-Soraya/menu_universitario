# apps/comedor/views.py
from django.contrib import messages
import datetime
from django.shortcuts import render, redirect
from .models import Estudiante, Platillo, Menu, Calificacion, Comentario
from .forms import EstudianteForm, PlatilloForm, MenuForm, CalificacionForm, ComentarioForm
from django.contrib import messages



# Estudiante CRUD

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'comedor/listar_estudiantes.html', {'estudiantes': estudiantes})


def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Estudiante guardado correctamente")
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'comedor/crear_estudiante.html', {'form': form})

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request,"Estudiante editado correctamente")
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'comedor/editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        estudiante.delete()
        messages.success(request,"Estudiante eliminado correctamente")
        return redirect('listar_estudiantes')
    return render(request, 'comedor/eliminar_estudiante.html', {'estudiante': estudiante})

# Platillo CRUD

def listar_platillos(request):
    platillos = Platillo.objects.all()
    return render(request, 'comedor/listar_platillos.html', {'platillos': platillos})

def crear_platillo(request):
    if request.method == "POST":
        form = PlatilloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Platillo guardado correctamente")
            return redirect('listar_platillos')
    else:
        form = PlatilloForm()
    return render(request, 'comedor/crear_platillo.html', {'form': form})

def editar_platillo(request, id):
    platillo = Platillo.objects.get(id=id)
    if request.method == "POST":
        form = PlatilloForm(request.POST, instance=platillo)
        if form.is_valid():
            form.save()
            messages.success(request,"Platillo editado correctamente")
            return redirect('listar_platillos')
    else:
        form = PlatilloForm(instance=platillo)
    return render(request, 'comedor/editar_platillo.html', {'form': form})

def eliminar_platillo(request, id):
    platillo = Platillo.objects.get(id=id)
    if request.method == "POST":
        platillo.delete()
        messages.success(request,"Platillo eliminado correctamente")
        return redirect('listar_platillos')
    return render(request, 'comedor/eliminar_platillo.html', {'platillo': platillo})

# Menu CRUD

def listar_menus(request):
    menus = Menu.objects.all()
    return render(request, 'comedor/listar_menus.html', {'menus': menus})

def crear_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            form.save_m2m()  # Guarda las relaciones ManyToMany
            messages.success(request,"Menú guardado correctamente")
            return redirect('listar_menus')
    else:
        form = MenuForm()
    return render(request, 'comedor/crear_menu.html', {'form': form})



def editar_menu(request, id):
    menu = Menu.objects.get(id=id)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            form.save_m2m()  # Guarda las relaciones ManyToMany actualizadas
            messages.success(request,"Menú editado correctamente")
            return redirect('listar_menus')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'comedor/editar_menu.html', {'form': form})

def eliminar_menu(request, id):
    menu = Menu.objects.get(id=id)
    if request.method == "POST":
        menu.delete()
        messages.success(request,"Menú eliminado correctamente")
        return redirect('listar_menus')
    return render(request, 'comedor/eliminar_menu.html', {'menu': menu})


# Calificacion CRUD

def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'comedor/listar_calificaciones.html', {'calificaciones': calificaciones})

def crear_calificacion(request):
    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Calificación guardada correctamente")
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'comedor/crear_calificacion.html', {'form': form})

def editar_calificacion(request, id):
    calificacion = Calificacion.objects.get(id=id)
    if request.method == "POST":
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request,"Calificación editada correctamente")
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'comedor/editar_calificacion.html', {'form': form})

def eliminar_calificacion(request, id):
    calificacion = Calificacion.objects.get(id=id)
    if request.method == "POST":
        calificacion.delete()
        messages.success(request,"Calificación eliminada correctamente")
        return redirect('listar_calificaciones')
    return render(request, 'comedor/eliminar_calificacion.html', {'calificacion': calificacion})

# Comentario CRUD

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comedor/listar_comentarios.html', {'comentarios': comentarios})

def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Comentario guardado correctamente")
            return redirect('listar_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'comedor/crear_comentario.html', {'form': form})

def editar_comentario(request, id):
    comentario = Comentario.objects.get(id=id)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request,"Comentario editado correctamente")
            return redirect('listar_comentarios')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'comedor/editar_comentario.html', {'form': form})

def eliminar_comentario(request, id):
    comentario = Comentario.objects.get(id=id)
    if request.method == "POST":
        comentario.delete()
        messages.success(request,"Comentario eliminado correctamente")
        return redirect('listar_comentarios')
    
    return render(request, 'comedor/eliminar_comentario.html', {'comentario': comentario})

#inicio
def inicio(request):
    return render(request,'comedor/inicio.html')

#menu del dia
def menu_del_dia(request):
    fecha_hoy = datetime.date.today()
    menu = Menu.objects.filter(fecha=fecha_hoy).first()  # Obtiene el menú del día si existe
    return render(request, 'comedor/menu_del_dia.html', {'menu': menu, 'fecha': fecha_hoy})