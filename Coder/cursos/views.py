from django.shortcuts import render
from django.views.generic import ListView
from cursos.models import Curso

# Create your views here.

def inicio(request):
    return render(request, "cursos/index.html")

class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "cursos/listar.html"

