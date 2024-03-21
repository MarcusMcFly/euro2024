# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # Importa settings.py para obtener AUTH_USER_MODEL

# Modelo para un Equipo de Fútbol
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50, blank=True)  # Opcional
    ciudad = models.CharField(max_length=50, blank=True)  # Opcional
    logo = models.ImageField(upload_to='logos_equipos/', blank=True, null=True)  # Opcional

    def __str__(self):
        return self.nombre

# Modelo para un Partido de Fútbol_
class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, related_name='partidos_como_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipo, related_name='partidos_como_visitante', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    lugar = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

# Modelo para la Apuesta
class Apuesta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    eleccion = models.CharField(max_length=100)  # Ejemplo: 'Local', 'Visitante', 'Empate'
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Apuesta de {self.usuario} en {self.partido}"

# Modelo para el Resultado de un Partido
class Resultado(models.Model):
    partido = models.OneToOneField(Partido, on_delete=models.CASCADE)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()

    def __str__(self):
        return f"Resultado: {self.partido} - {self.goles_local}:{self.goles_visitante}"


# Modelo de Usuario extendido
class Usuario(AbstractUser):
    # Añade campos adicionales aquí
    fecha_nacimiento = models.DateField(null=True, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username


