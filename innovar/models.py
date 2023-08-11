from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class UsuarioCustomizado(AbstractUser):
    eh_atendente = models.BooleanField(default=False)
    eh_cliente = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14, unique=True)
    numero_telefone = models.CharField(max_length=15)
   

    class Meta:
        permissions = [
            ("can_add_cliente_procedimento", "Can add ClienteProcedimento"),
            ("can_change_cliente_procedimento", "Can change ClienteProcedimento"),
        ]

    def __str__(self):
        return self.get_full_name()


class Atendente(models.Model):
    usuario = models.OneToOneField(UsuarioCustomizado, on_delete=models.CASCADE, primary_key=True, default=1    )

    def __str__(self):
        return str(self.usuario)


class Cliente(models.Model):
    usuario = models.OneToOneField(UsuarioCustomizado, on_delete=models.CASCADE, primary_key=True)
    idade = models.PositiveIntegerField()
    prescricao_medica = models.TextField(blank=True, null=True)
    possui_problema_fisico = models.BooleanField(default=False)
    possui_problema_cardiaco = models.BooleanField(default=False)
    possui_problema_respiratorio = models.BooleanField(default=False)
    possui_alergia = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario)

class HorarioBloqueado(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    atendentes = models.ManyToManyField(Atendente, related_name='horarios_bloqueados') 

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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='procedimentos')  # Adicione related_name
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, related_name='clientes')  # Adicione related_name
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
    cpf_superior = models.CharField(max_length=14)  # CPF do superior


    def __str__(self):
        return self.chave
