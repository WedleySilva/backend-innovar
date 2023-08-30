from django.db import models

class HorarioBloqueado(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia} - {self.hora_inicio} às {self.hora_fim}"