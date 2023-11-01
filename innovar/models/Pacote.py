from django.db import models
from django.utils.translation import gettext_lazy as _

class Pacote(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='pacotes/', null=True, blank=True)

    def __str__(self):
        return self.nome
