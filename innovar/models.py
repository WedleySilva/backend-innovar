from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

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

class HorarioBloqueado(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia} - {self.hora_inicio} às {self.hora_fim}"

class Procedimento(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pacote(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class ClienteProcedimento(models.Model):
    cliente = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    sessoes_total = models.PositiveIntegerField()
    sessoes_completas = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('cliente', 'procedimento')

    def clean(self):
        if self.cliente and not self.cliente.eh_cliente:
            raise ValidationError("Apenas clientes podem ser associados a procedimentos.")
        if self.sessoes_completas > self.sessoes_total:
            raise ValidationError("O número de sessões completas não pode ser maior que o total de sessões.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente} - {self.procedimento}"

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

cliente_group, created_cliente = Group.objects.get_or_create(name='Cliente')
atendente_group, created_atendente = Group.objects.get_or_create(name='Atendente')
admin_group, created_admin = Group.objects.get_or_create(name='Admin')

@receiver(post_save, sender=UsuarioCustomizado)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.eh_cliente:
            instance.groups.add(cliente_group)
        if instance.eh_atendente:
            instance.groups.add(atendente_group)
        if instance.is_staff: 
            instance.groups.add(admin_group)

# class ChavePermissao(models.Model):
#     chave = models.CharField(max_length=14, unique=True)
#     cpf_superior = models.CharField(max_length=14)

#     def __str__(self):
#         return self.chave

# class Desconto(models.Model):
#     cliente = models.ForeignKey(UsuarioCustomizado, on_delete=models.CASCADE, limit_choices_to={'eh_cliente': True})
#     TIPOS_DESCONTO = [('dinheiro', 'Dinheiro'), ('porcentagem', 'Porcentagem')]
#     tipo_desconto = models.CharField(choices=TIPOS_DESCONTO, max_length=15)
#     procedimento = models.ForeignKey(Procedimento, blank=True, null=True, on_delete=models.SET_NULL)
#     pacote = models.ForeignKey(Pacote, blank=True, null=True, on_delete=models.SET_NULL)
#     valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
#     percentual_desconto = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
#     chave_permissao = models.ForeignKey(ChavePermissao, on_delete=models.SET_NULL, blank=True, null=True)

#     def clean(self):
#         if not self.valor_desconto and not self.percentual_desconto:
#             raise ValidationError("É necessário preencher pelo menos um dos campos de desconto.")
#         if self.valor_desconto and self.percentual_desconto:
#             raise ValidationError("Apenas um campo de desconto (valor em dinheiro ou percentual) deve ser preenchido.")
#         if self.tipo_desconto == 'dinheiro':
#             if self.valor_desconto and self.valor_desconto > self.get_max_valor_desconto():
#                 raise ValidationError("O valor do desconto em dinheiro não pode ser maior que o valor registrado no plano ou procedimento escolhido.")
#         elif self.tipo_desconto == 'porcentagem' and (not self.percentual_desconto or self.percentual_desconto > 100):
#             raise ValidationError("O desconto em porcentagem deve estar entre 0 e 100.")
#         if self.chave_permissao and self.cliente.cpf != self.chave_permissao.cpf_superior:
#             raise ValidationError("O CPF do cliente não corresponde ao CPF registrado na chave de permissão.")

#     def get_max_valor_desconto(self):
#         if self.procedimento:
#             return self.procedimento.preco
#         elif self.pacote:
#             return self.pacote.preco
#         return 0

#     def save(self, *args, **kwargs):
#         self.clean()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Desconto para {self.cliente}"