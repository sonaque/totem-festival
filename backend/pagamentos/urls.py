from django.contrib import admin
from django.urls import path, include
from .views import iniciar_pagamento, confirmar_pagamento

urlpatterns = [
    path('', iniciar_pagamento, name = 'iniciar_pagamento'),
    path('webhook/', confirmar_pagamento, name='webhook'),
]
