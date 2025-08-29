from django.shortcuts import render

def estudiantes_view(request):
    return render(request, 'principal/estudiantes.html')

def administradores_view(request):
    return render(request, 'principal/administradores.html')