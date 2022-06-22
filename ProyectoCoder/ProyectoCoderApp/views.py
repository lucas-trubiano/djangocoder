import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    # post
    if request.method == "POST":

        info_formulario = request.POST
        
        curso = Curso(info_formulario["nombre"], info_formulario["comision"])

        curso.save()
        
        return render(request,"ProyectoCoderApp/formulario_curso.html",{})

    else: # get y otros
        return render(request,"ProyectoCoderApp/formulario_curso.html",{})
    

def profesores(request):
    return render(request,"ProyectoCoderApp/profesores.html",{})

def estudiantes(request):
    return render(request,"ProyectoCoderApp/estudiantes.html",{})

def cursos(request):
    # return HttpResponse("Vista de cursos")

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")