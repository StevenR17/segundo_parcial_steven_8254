from django.urls import path
from .views import (ProfesorListView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
                     MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView)
from .views import home

urlpatterns = [
    path('home/', home, name='home'),

#URLS PARA PROFESORES
    path('profesores/', ProfesorListView.as_view(), name='profesor_list'),
    path('profesores/nuevo/', ProfesorCreateView.as_view(), name='profesor_create'),
    path('profesores/editar/<str:pk>/', ProfesorUpdateView.as_view(), name='profesor_update'),
    path('profesores/eliminar/<str:pk>/', ProfesorDeleteView.as_view(), name='profesor_delete'),

#URLS PARA MASCOTAS
    path('mascotas/', MascotaListView.as_view(), name='mascota_list'),
    path('mascotas/nueva/', MascotaCreateView.as_view(), name='mascota_create'),
    path('mascotas/editar/<int:pk>/', MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascotas/eliminar/<int:pk>/', MascotaDeleteView.as_view(), name='mascota_delete'),
]

