from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiantes_view, name='estudiantes'),
    path('administradores/', views.administradores_view, name='administradores'),
]