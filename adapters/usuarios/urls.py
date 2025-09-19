from rest_framework.views import APIView
from .views import CadastrarUsuarioView
from django.urls import path

urlpatterns = [
    path('criar/', CadastrarUsuarioView.as_view(), name='criar-usuarios'),
]