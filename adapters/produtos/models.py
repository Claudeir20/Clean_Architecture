from django.db import models

# Create your models here.

class ProdutoMoedl(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    vendedor_id = models.IntegerField()