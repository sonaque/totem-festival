from django.urls import path, include
from . import views
# from .views import UsuarioCreateView 


urlpatterns = [
    path('registrar/', views.registrar_pulseira, name = 'registrar_pulseira')
    # path('registro/', mostrar_registro, name = 'registro'),
    # path('registrar/', UsuarioCreateView.as_view(), name = 'registrar_usuario')
]