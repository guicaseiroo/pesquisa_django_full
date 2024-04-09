from django.contrib import admin
from .models import Pergunta, Resposta


class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 1

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta)