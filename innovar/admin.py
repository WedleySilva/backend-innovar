from django.contrib import admin
from .models import Procedimento, Pacote, HorarioBloqueado

class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')


class HorarioBloqueadoAdmin(admin.ModelAdmin): 
    list_display = ('dia', 'hora_inicio', 'hora_fim')

admin.site.register(Procedimento, ProcedimentoAdmin)
admin.site.register(Pacote, PacoteAdmin)
admin.site.register(HorarioBloqueado, HorarioBloqueadoAdmin)
