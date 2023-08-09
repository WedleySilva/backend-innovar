from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('client', 'Cliente'),
        ('manager', 'Gerente'),
        ('professional', 'Profissional'),
        ('attendant', 'Atendente'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class Cliente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cliente')
    idade = models.PositiveIntegerField()
    prescricao_medica = models.TextField(blank=True)

class Gerente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    senha_especial = models.CharField(max_length=100)

class Profissional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)

class Atendente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
