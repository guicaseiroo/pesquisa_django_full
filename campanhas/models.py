from django.db import models
from django.utils import timezone

class Campanha(models.Model):
    campanha_nome = models.CharField(max_length=100)
    campanha_descricao = models.TextField()
    campanha_data_hora_validade = models.DateTimeField()
    campanha_imagem = models.ImageField(upload_to='imagens_campanha/', blank=True) 
    campanha_fundo = models.ImageField(upload_to='imagens_campanha_fundo/', blank=True) 


    def __str__(self):
        return self.campanha_nome

    def campanha_valida(self):
        return timezone.now() < self.campanha_data_hora_validade
