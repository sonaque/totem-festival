from django.contrib import admin
from django.urls import path, include
from .views import ingressos1, cadastro
from pagamentos import urls as pagamentos_urls

urlpatterns = [
    path('', ingressos1, name = 'ingressos1'),
    path('cadastro/', cadastro, name = 'cadastro'),
    # path('ingressos_vip_1/', ingressos_vip_1, name = 'ingressos_vip_1'),
    path('cadastro/pagamento/', include(pagamentos_urls), name = 'pagamento_pista'),
]
