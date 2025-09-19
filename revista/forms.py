from django import forms
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

class EstudiantePublicadorForm(forms.ModelForm):
    class Meta:
        model = EstudiantePublicador
        fields = "__all__"

class EstudianteAutorizadorForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizador
        fields = "__all__"

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = "__all__"
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 5}),
            "fecha_publicacion": forms.DateInput(attrs={"type": "date"}),
        }
