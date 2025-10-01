from django.urls import path
from . import views

app_name = "principal"
urlpatterns = [
    path('estudiantes/', views.estudiantes_view, name='estudiantes'),
    path('administradores/', views.administradores_view, name='administradores'),
    path("estudiantes/<int:pk>/detalle/", views.EstudianteDetailView.as_view(), name="estudiante_detalle"),
    path("estudiantes/<int:pk>/editar/", views.EstudianteUpdateView.as_view(), name="estudiante_editar"),
    path("administradores/<int:pk>/detalle/", views.AdministradorDetailView.as_view(), name="administrador_detalle"),
    path("administradores/<int:pk>/editar/", views.AdministradorUpdateView.as_view(), name="administrador_editar"),
]