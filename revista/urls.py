from django.urls import path
from .views import (
    PublicadorListView, PublicadorCreateView, PublicadorUpdateView, PublicadorDeleteView,
    AutorizadorListView, AutorizadorCreateView, AutorizadorUpdateView, AutorizadorDeleteView,
    PublicacionListView, PublicacionCreateView, PublicacionUpdateView, PublicacionDeleteView
)
app_name = "revista"

urlpatterns = [
    # Publicadores
    path("publicadores/", PublicadorListView.as_view(), name="lista_publicadores"),
    path("publicadores/nuevo/", PublicadorCreateView.as_view(), name="publicadores_create"),
    path("publicadores/<int:pk>/editar/", PublicadorUpdateView.as_view(), name="publicadores_update"),
    path("publicadores/<int:pk>/eliminar/", PublicadorDeleteView.as_view(), name="publicadores_delete"),

    # Autorizadores
    path("autorizadores/", AutorizadorListView.as_view(), name="lista_autorizadores"),
    path("autorizadores/nuevo/", AutorizadorCreateView.as_view(), name="autorizadores_create"),
    path("autorizadores/<int:pk>/editar/", AutorizadorUpdateView.as_view(), name="autorizadores_update"),
    path("autorizadores/<int:pk>/eliminar/", AutorizadorDeleteView.as_view(), name="autorizadores_delete"),

    # Publicaciones
    path("publicaciones/", PublicacionListView.as_view(), name="lista_publicaciones"),
    path("publicaciones/nueva/", PublicacionCreateView.as_view(), name="publicaciones_create"),
    path("publicaciones/<int:pk>/editar/", PublicacionUpdateView.as_view(), name="publicaciones_update"),
    path("publicaciones/<int:pk>/eliminar/", PublicacionDeleteView.as_view(), name="publicaciones_delete"),
]