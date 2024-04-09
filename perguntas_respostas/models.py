from django.db import models
from campanhas.models import Campanha

class Pergunta(models.Model):
    pergunta_campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pergunta_texto = models.CharField(max_length=100)

    def __str__(self):
        return self.pergunta_texto

class Resposta(models.Model):
    resposta_pergunta = models.ForeignKey(Pergunta, related_name='respostas', on_delete=models.CASCADE)
    resposta_texto = models.CharField(max_length=100)

    def __str__(self):
        return self.resposta_texto