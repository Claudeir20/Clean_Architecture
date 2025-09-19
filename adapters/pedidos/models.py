from django.db import models
from adapters.usuarios.models import UsuarioModel

# Create your models here.

class PedidoModel(models.Model):
    cliente_id= models.IntegerField()
    status = models.CharField(max_length=20, default="pendente")
    total = models.DecimalField(max_digits=10, decimal_places=2)

