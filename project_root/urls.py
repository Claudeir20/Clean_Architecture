
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/produtos/', include('adapters.produtos.urls')),
    path('api/usuarios/', include('adapters.usuarios.urls')),
    path('api/pedidos/', include('adapters.pedidos.urls')),
]
