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
from usuarios import urls as usuarios_urls
from eventos import views
from .view import pagina_principal, mapa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal),
    path('api/', include(eventos_urls)),
    path('mapa/', mapa, name = 'mapa')
    # path('api/usuarios/', include(usuarios_urls))
]
