from django.contrib import admin
from .models import (Atendente, ChavePermissao, Cliente, ClientePacote, ClienteProcedimento, HorarioBloqueado, Pacote, Procedimento, UsuarioCustomizado)

@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(ChavePermissao)
class ChavePermissaoAdmin(admin.ModelAdmin):
    list_display = ('chave', 'cpf_superior')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'idade', 'prescricao_medica', 'cpf', 'numero_telefone', 'possui_problema_fisico',
                    'possui_problema_cardiaco', 'possui_problema_respiratorio', 'possui_alergia')

@admin.register(ClientePacote)
class ClientePacoteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'pacote')

@admin.register(ClienteProcedimento)
class ClienteProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'procedimento', 'sessoes_total', 'sessoes_completas')

@admin.register(HorarioBloqueado)
class HorarioBloqueadoAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora_inicio', 'hora_fim')

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

@admin.register(UsuarioCustomizado)
class UsuarioCustomizadoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'eh_atendente', 'eh_cliente', 'cpf', 'numero_telefone')
