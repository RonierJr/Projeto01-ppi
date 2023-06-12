from django.shortcuts import render
from .models import Curso
from django.shortcuts import get_object_or_404

# Create your views here.

def detalhe_cursos(request,id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    context={
        'objeto' : curso,
    }
    return render(request,'publicacao/detalhe.html',context)

def index(request):
    return render(request,'publicacao/index.html')

def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {
        'lista_cursos' : cursos 
    } 
    return render(request,'publicacao/cursos.html',context)