from django.urls import path
from cursos import views

urlpatterns = [
    path("", views.inicio),
    path("listar/", views.CursoListView.as_view(), name="ListarCursos")
]