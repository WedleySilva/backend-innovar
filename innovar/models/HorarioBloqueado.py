
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class HorarioBloqueado(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia} - {self.hora_inicio} às {self.hora_fim}"

    def clean(self):
        if self.hora_inicio >= self.hora_fim:
            raise ValidationError("O horário de início deve ser menor que o horário de fim.")

        existent_records = HorarioBloqueado.objects.filter(
            dia=self.dia,
            hora_inicio=self.hora_inicio,
            hora_fim=self.hora_fim
        ).exclude(pk=self.pk)  
        if existent_records.exists():
            raise ValidationError("Este horário já está bloqueado.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

