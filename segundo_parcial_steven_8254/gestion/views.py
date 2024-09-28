from django.shortcuts import render, get_object_or_404 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor, Mascota
from django.contrib.auth.decorators import login_required


# Create your views here.
"""""
#VISTAS PARA PROFESORES
class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = 'gestion/profesor_list.html'

class ProfesorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Profesor
    fields = ['cedula', 'nombre', 'apellido', 'genero']
    template_name = 'gestion/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.add_profesor'

class ProfesorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'genero']
    template_name = 'gestion/profesor_form.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.change_profesor'

class ProfesorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Profesor
    template_name = 'gestion/profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor_list')
    permission_required = 'gestion.delete_profesor'

#VISTAS PARA MASCOTAS
class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'gestion/mascota_list.html'
    context_object_name = 'mascotas'

class MascotaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mascota
    fields = ['nombre', 'raza', 'genero', 'cedula']
    template_name = 'gestion/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.add_mascota'

class MascotaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mascota
    fields = ['nombre', 'raza', 'genero', 'cedula']
    template_name = 'gestion/mascota_form.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.change_mascota'

class MascotaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'gestion/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_list')
    permission_required = 'gestion.delete_mascota'
"""

# views.py
from rest_framework import generics
from rest_framework import filters
from .models import Profesor, Mascota
from .serializers import ProfesorSerializer, MascotaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .forms import MascotaForm, ProfesorForm  # Asegúrate de que esta línea esté presente al inicio del archivo views.py



class ProfesorListCreate(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['nombre', 'apellido']  # Cambia esto según tus campos

class ProfesorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class MascotaListCreate(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['nombre', 'raza']  # Cambia esto según tus campos

class MascotaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer



# Vista de listado de Profesores (HTML)
@login_required
def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'gestion/profesor_list.html', {'object_list': profesores})

# Vista de listado de Mascotas (HTML)
@login_required
def mascota_list(request):
    mascotas = Mascota.objects.all()
    return render(request, 'gestion/mascota_list.html', {'object_list': mascotas})

#VISTA HOME
@login_required
def home(request):
    return render(request, 'gestion/home.html')



# Vistas para ver un profesor
@login_required
def profesor_detail(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'gestion/profesor_detail.html', {'profesor': profesor})

# Vista para editar un profesor
@login_required
def profesor_edit(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == "POST":
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect(reverse('profesor-list'))  # Redirige a la lista de profesores
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'gestion/profesor_form.html', {'form': form})

# Vista para eliminar un profesor
@login_required
def profesor_delete(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == "POST":
        profesor.delete()
        return redirect(reverse('profesor-list'))  # Redirige a la lista de profesores
    return render(request, 'gestion/profesor_confirm_delete.html', {'profesor': profesor})

# Vistas para ver una mascota
@login_required
def mascota_detail(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request, 'gestion/mascota_detail.html', {'mascota': mascota})

# Vista para editar una mascota
@login_required
def mascota_edit(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect(reverse('mascota-list'))  # Redirige a la lista de mascotas
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'gestion/mascota_form.html', {'form': form})

# Vista para eliminar una mascota
@login_required
def mascota_delete(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        mascota.delete()
        return redirect(reverse('mascota-list'))  # Redirige a la lista de mascotas
    return render(request, 'gestion/mascota_confirm_delete.html', {'mascota': mascota})




