from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Definimos los modelos
class Profesor(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    cedula = models.ForeignKey('Profesor', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"


