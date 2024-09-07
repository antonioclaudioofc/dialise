from django.contrib import admin
from .models import Sexo, Acesso, Dialise, Paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'diagnostico_principal', 'contato', 'mostrar',) #mostrar
    list_display_links = ('nome',)
    list_filter = ('nome',)
    list_editable = ('contato', 'mostrar')
    search_fields = ('nome',)
    

admin.site.register(Sexo)
admin.site.register(Acesso)
admin.site.register(Dialise)
admin.site.register(Paciente, PacienteAdmin)
