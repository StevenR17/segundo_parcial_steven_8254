from django.urls import path
"""""
from .views import (ProfesorListView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
                     MascotaListView, MascotaCreateView, MascotaUpdateView, MascotaDeleteView)
"""

from .views import home, profesor_list, mascota_list

from .views import (
    home, profesor_list, mascota_list,
    profesor_detail, profesor_edit, profesor_delete,
    mascota_detail, mascota_edit, mascota_delete,
    ProfesorListCreate, ProfesorRetrieveUpdateDestroy,
    MascotaListCreate, MascotaRetrieveUpdateDestroy,
)

urlpatterns = [
    path('home/', home, name='home'),

     # URLs para la API de profesores
    path('profesores/', ProfesorListCreate.as_view(), name='profesor-list-create'),  # Listar y crear (API)
    path('profesores/<int:pk>/', ProfesorRetrieveUpdateDestroy.as_view(), name='profesor-detail'),  # Ver, editar, eliminar (API)

    # URLs para la API de mascotas
    path('mascotas/', MascotaListCreate.as_view(), name='mascota-list-create'),  # Listar y crear (API)
    path('mascotas/<int:pk>/', MascotaRetrieveUpdateDestroy.as_view(), name='mascota-detail'),  # Ver, editar, eliminar (API)

    # URLs para vistas HTML
    path('profesores/listar/', profesor_list, name='profesor-list'),  # Listar profesores (HTML)
    path('mascotas/listar/', mascota_list, name='mascota-list'),  # Listar mascotas (HTML)

    
    # URLs para ver, editar y eliminar profesores
    path('profesores/<int:pk>/', profesor_detail, name='profesor-detail'),  # Ver profesor
    path('profesores/<int:pk>/editar/', profesor_edit, name='profesor-edit'),  # Editar profesor
    path('profesores/<int:pk>/eliminar/', profesor_delete, name='profesor-delete'),  # Eliminar profesor

    # URLs para ver, editar y eliminar mascotas
    path('mascotas/<int:pk>/', mascota_detail, name='mascota-detail'),  # Ver mascota
    path('mascotas/<int:pk>/editar/', mascota_edit, name='mascota-edit'),  # Editar mascota
    path('mascotas/<int:pk>/eliminar/', mascota_delete, name='mascota-delete'),  # Eliminar mascota
]

