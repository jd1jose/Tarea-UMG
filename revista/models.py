from django.db import models

# Estudiantes que publican
class EstudiantePublicador(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    carnet = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.carnet})"


# Estudiantes que autorizan
class EstudianteAutorizador(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    carnet = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.carnet})"


# Publicaciones
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    publicador = models.ForeignKey(
        EstudiantePublicador, on_delete=models.CASCADE, related_name="publicaciones"
    )
    autorizador = models.ForeignKey(
        EstudianteAutorizador, on_delete=models.PROTECT, related_name="autorizaciones"
    )

    def __str__(self):
        return self.titulo


# Create your models here.
