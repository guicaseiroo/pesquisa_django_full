from django.db import models
from campanhas.models import Campanha
from perguntas_respostas.models import Pergunta

class RespostaUsuario(models.Model):
    email = models.EmailField()
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta_texto = models.TextField() 
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.campanha.nome}"