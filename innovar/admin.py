from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cliente, Gerente, Profissional, Atendente

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type')
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil', {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Profissional)
admin.site.register(Atendente)
