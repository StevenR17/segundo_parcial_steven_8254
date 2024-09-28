from django.shortcuts import render, get_object_or_404 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor, Mascota
from django.contrib.auth.decorators import login_required


# Create your views here.

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


#VISTA HOME
@login_required
def home(request):
    return render(request, 'gestion/home.html')