from django.contrib import admin
from .models import UsuarioCustomizado, Procedimento, Pacote, ClienteProcedimento, ClientePacote

class ClienteProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'procedimento', 'sessoes_total', 'sessoes_completas')
    
    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
            obj.save()
        except ValidationError as e:
            form.add_error(None, e)

class ClientePacoteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'pacote', 'sessoes_total', 'sessoes_completas')
    
    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()
            obj.save()
        except ValidationError as e:
            form.add_error(None, e)

class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class UsuarioCustomizadoAdmin(admin.ModelAdmin):
    list_display = ('username', 'cpf', 'numero_telefone', 'idade', 'prescricao_medica', 'possui_problema_fisico', 'possui_problema_cardiaco', 'possui_problema_respiratorio', 'possui_alergia', 'eh_atendente', 'eh_cliente')

admin.site.register(UsuarioCustomizado, UsuarioCustomizadoAdmin)
admin.site.register(Procedimento, ProcedimentoAdmin)
admin.site.register(Pacote, PacoteAdmin)
admin.site.register(ClienteProcedimento, ClienteProcedimentoAdmin)
admin.site.register(ClientePacote, ClientePacoteAdmin)
