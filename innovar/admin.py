from django.contrib import admin
from .models import UsuarioCustomizado, Atendente, Cliente, HorarioBloqueado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, ChavePermissao, Desconto

@admin.register(UsuarioCustomizado)
class UsuarioCustomizadoAdmin(admin.ModelAdmin):
    list_display = ('username', 'cpf', 'eh_atendente', 'eh_cliente')

@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'idade', 'cpf', 'numero_telefone', 'possui_problema_fisico', 'possui_problema_cardiaco', 'possui_problema_respiratorio', 'possui_alergia')

@admin.register(HorarioBloqueado)
class HorarioBloqueadoAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora_inicio', 'hora_fim')

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

@admin.register(ClienteProcedimento)
class ClienteProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'procedimento', 'sessoes_total', 'sessoes_completas')

@admin.register(ClientePacote)
class ClientePacoteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'pacote', 'sessoes_total', 'sessoes_completas')

@admin.register(ChavePermissao)
class ChavePermissaoAdmin(admin.ModelAdmin):
    list_display = ('chave', 'atendente')

@admin.register(Desconto)
class DescontoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipo', 'valor', 'data_aplicacao')
