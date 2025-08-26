"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eventos import urls as eventos_urls
from ingressos import urls as ingressos_urls
from usuarios import urls as usuarios_urls
from bar import urls as bar_urls
from eventos import views
from .view import pagina_principal, mapa, programacao, bar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal,name='pagina_principal'),
    path('mapa/', mapa, name = 'mapa'),
    path('programacao/', programacao, name = 'programacao'),
    path('ingressos/', include(ingressos_urls)),
    # path('registrar/', registrar_usuario, name = 'registrar'),
    path('usuarios/', include(usuarios_urls)),
    path('bar/', include(bar_urls))
    
    # path('api/', include(eventos_urls)),
    # path('api/usuarios/', include(usuarios_urls))
]
