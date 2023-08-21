from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserManager, UsuarioCustomizado, HorarioBloqueado, Procedimento, Pacote, ClienteProcedimento, ClientePacote, ChavePermissao

admin.site.register(UsuarioCustomizado)
admin.site.register(HorarioBloqueado)
admin.site.register(Procedimento)
admin.site.register(Pacote)
admin.site.register(ClienteProcedimento)
admin.site.register(ClientePacote)
admin.site.register(ChavePermissao)


# admin.site.unregister(Group)
