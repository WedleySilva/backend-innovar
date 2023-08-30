from django.db import models
from .usuario_customizado import UsuarioCustomizado
from .pacote import Pacote
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class ClientePacote(models.Model):
    cliente = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE)
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    sessoes_total = models.PositiveIntegerField()
    sessoes_completas = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('cliente', 'pacote')

    def clean(self):
        if self.cliente and not self.cliente.eh_cliente:
            raise ValidationError("Apenas clientes podem ser associados a pacotes.")
        if self.sessoes_completas > self.sessoes_total:
            raise ValidationError("O número de sessões completas não pode ser maior que o total de sessões.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente} - {self.pacote}"