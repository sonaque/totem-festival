from django.urls import path, include
from .views import pagina_bar
from pagamentos.views import iniciar_pagamento_produto

urlpatterns = [
    path('', pagina_bar, name= 'pagina_bar'),
    path('pagamento/<int:produto_id>/', iniciar_pagamento_produto, name='iniciar_pagamento_produto')
]
