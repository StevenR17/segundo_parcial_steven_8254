# forms.py
from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'genero', 'cedula']  # Asegúrate de que estos son los campos que deseas usar


# forms.py
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['cedula', 'nombre', 'apellido', 'genero']  # Asegúrate de que estos son los campos que deseas usar
