from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from .custom_user_manager import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class UsuarioCustomizado(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    numero_telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(null=True, blank=True)
    prescricao_medica = models.TextField(blank=True, null=True)
    possui_problema_fisico = models.BooleanField(default=False)
    possui_problema_cardiaco = models.BooleanField(default=False)
    possui_problema_respiratorio = models.BooleanField(default=False)
    possui_alergia = models.BooleanField(default=False)
    eh_atendente = models.BooleanField(default=False)
    eh_cliente = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()
    
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.eh_cliente:
            instance.groups.add(cliente_group)
        if instance.eh_atendente:
            instance.groups.add(atendente_group)
        if instance.is_staff: 
            instance.groups.add(admin_group)

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(username)
        user = self.model(username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(username, password, **extra_fields)
    
@receiver(post_save, sender=UsuarioCustomizado)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.eh_cliente:
            instance.groups.add(cliente_group)
        if instance.eh_atendente:
            instance.groups.add(atendente_group)
        if instance.is_staff: 
            instance.groups.add(admin_group)