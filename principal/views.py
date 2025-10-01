from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from revista.models import EstudiantePublicador, EstudianteAutorizador
from revista.forms import EstudiantePublicadorForm, EstudianteAutorizadorForm

def estudiantes_view(request):
    return render(request, 'principal/estudiantes.html')

def administradores_view(request):
    return render(request, 'principal/administradores.html')

def estudiantes_view(request):
    if request.method == "POST":
        form = EstudiantePublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("principal:estudiantes")
    else:
        form = EstudiantePublicadorForm()

    estudiantes = EstudiantePublicador.objects.all()
    return render(request, "principal/estudiantes.html", {
        "form": form,
        "estudiantes": estudiantes
    })

def administradores_view(request):
    if request.method == "POST":
        form = EstudianteAutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("principal:administradores")
    else:
        form = EstudianteAutorizadorForm()

    administradores = EstudianteAutorizador.objects.all()
    return render(request, "principal/administradores.html", {
        "form": form,
        "administradores": administradores
    })

# Detalle
class EstudianteDetailView(DetailView):
    model = EstudiantePublicador
    template_name = "principal/estudiante_detalle.html"
    context_object_name = "estudiante"

class AdministradorDetailView(DetailView):
    model = EstudianteAutorizador
    template_name = "principal/administrador_detalle.html"
    context_object_name = "administradores"

# Edición
class EstudianteUpdateView(UpdateView):
    model = EstudiantePublicador
    fields = "__all__"
    template_name = "principal/estudiante_editar.html"
    success_url = reverse_lazy("principal:estudiantes")

class AdministradorUpdateView(UpdateView):
    model = EstudianteAutorizador
    fields = "__all__"
    template_name = "principal/administrador_editar.html"
    success_url = reverse_lazy("principal:administradores")