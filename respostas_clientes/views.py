from django.shortcuts import render, get_object_or_404
from perguntas_respostas.models import Resposta, Pergunta
from .models import Campanha, RespostaUsuario
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from .utils import encrypt_email, decrypt_email



def cript(request):
    email = 'hello_word@gmail.com'  # O e-mail que você quer passar
    encrypted_email = encrypt_email(email)
    # Agora você pode passar encrypted_email na URL
    return HttpResponse(encrypted_email)

def apresentacao_campanha(request, campanha_id, email):
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    if campanha.campanha_data_hora_validade < timezone.now():
        return render(request, 'acabou.html')
    return render(request, 'index.html', {'campanha': campanha, 'email': email,})

def detalhes_campanha(request, campanha_id, email):
    email = decrypt_email(email)
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    perguntas = Pergunta.objects.filter(pergunta_campanha=campanha).prefetch_related('respostas')
    return render(request, 'pesquisa.html', {'campanha': campanha, 'perguntas': perguntas, 'email': email,})

def sucesso_campanha(request, campanha_id, email):
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    #email_push = decrypt_email(email)
    
    if request.method == 'POST':
        #email = request.POST.get('email', 'anonimo@example.com')
        for key, value in request.POST.items():
            if key.startswith('resposta_'):
                pergunta_id = key.split('_')[-1]
                resposta_id = value
                resposta_texto = Resposta.objects.get(pk=resposta_id).resposta_texto

                RespostaUsuario.objects.create(
                    email=email,
                    campanha=campanha,
                    pergunta_id=pergunta_id,
                    resposta_texto=resposta_texto 
                )

    return render(request, 'fim_pesquisa.html', {'campanha': campanha_id, 'email': email})
