from django.db import models

class Pacote(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome