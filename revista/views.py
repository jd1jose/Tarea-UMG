from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion
from .forms import EstudiantePublicadorForm, EstudianteAutorizadorForm, PublicacionForm

# -------- Publicadores --------
class PublicadorListView(ListView):
    model = EstudiantePublicador
    template_name = "revista/lista_publicadores.html"

class PublicadorCreateView(CreateView):
    model = EstudiantePublicador
    form_class = EstudiantePublicadorForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:publicadores_list")

class PublicadorUpdateView(UpdateView):
    model = EstudiantePublicador
    form_class = EstudiantePublicadorForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:publicadores_list")

class PublicadorDeleteView(DeleteView):
    model = EstudiantePublicador
    template_name = "revista/confirm_delete.html"
    success_url = reverse_lazy("revista:publicadores_list")


# -------- Autorizadores --------
class AutorizadorListView(ListView):
    model = EstudianteAutorizador
    template_name = "revista/lista_autorizadores.html"

class AutorizadorCreateView(CreateView):
    model = EstudianteAutorizador
    form_class = EstudianteAutorizadorForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:autorizadores_list")

class AutorizadorUpdateView(UpdateView):
    model = EstudianteAutorizador
    form_class = EstudianteAutorizadorForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:autorizadores_list")

class AutorizadorDeleteView(DeleteView):
    model = EstudianteAutorizador
    template_name = "revista/confirm_delete.html"
    success_url = reverse_lazy("revista:autorizadores_list")


# -------- Publicaciones --------
class PublicacionListView(ListView):
    model = Publicacion
    template_name = "revista/lista_publicaciones.html"

class PublicacionCreateView(CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:publicaciones_list")

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "revista/form.html"
    success_url = reverse_lazy("revista:publicaciones_list")

class PublicacionDeleteView(DeleteView):
    model = Publicacion
    template_name = "revista/confirm_delete.html"
    success_url = reverse_lazy("revista:publicaciones_list")
