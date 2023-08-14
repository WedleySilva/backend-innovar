from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

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

class UsuarioCustomizado(AbstractUser):
    eh_atendente = models.BooleanField(default=False)
    eh_cliente = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14, unique=True)
    numero_telefone = models.CharField(max_length=15)

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()

class Cliente(models.Model):
    usuario = models.OneToOneField(
        UsuarioCustomizado,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'eh_atendente': False}
    )
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    numero_telefone = models.CharField(max_length=15, unique=True)
    prescricao_medica = models.TextField(blank=True, null=True)
    possui_problema_fisico = models.BooleanField(default=False)
    possui_problema_cardiaco = models.BooleanField(default=False)
    possui_problema_respiratorio = models.BooleanField(default=False)
    possui_alergia = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario)

# Resto do seu código...

# Sinal para atualizar Cliente quando UsuarioCustomizado é atualizado
@receiver(post_save, sender=UsuarioCustomizado)
def update_cliente_from_usuario(sender, instance, **kwargs):
    try:
        cliente = Cliente.objects.get(usuario=instance)
        cliente.idade = instance.idade
        cliente.possui_problema_fisico = instance.possui_problema_fisico
        cliente.possui_problema_cardiaco = instance.possui_problema_cardiaco
        cliente.possui_problema_respiratorio = instance.possui_problema_respiratorio
        cliente.possui_alergia = instance.possui_alergia
        cliente.cpf = instance.cpf
        cliente.numero_telefone = instance.numero_telefone
        cliente.save()
    except Cliente.DoesNotExist:
        pass


class Atendente(models.Model):
    usuario = models.OneToOneField(UsuarioCustomizado, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.usuario)

class HorarioBloqueado(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField() 

    def __str__(self):
        return f"{self.dia} - {self.hora_inicio} às {self.hora_fim}"

class Procedimento(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class ClienteProcedimento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='procedimentos')
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, related_name='clientes')
    sessoes_total = models.PositiveIntegerField()
    sessoes_completas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cliente} - {self.procedimento}"

class ClientePacote(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pacotes')
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return f"{self.cliente} - {self.pacote}"

class ChavePermissao(models.Model):
    chave = models.CharField(max_length=14, unique=True)
    cpf_superior = models.CharField(max_length=14)  

    def __str__(self):
        return self.chave