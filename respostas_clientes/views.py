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

"""
def detalhes_campanha(request, campanha_id, email):
    email = decrypt_email(email)
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    perguntas = Pergunta.objects.filter(pergunta_campanha=campanha).prefetch_related('respostas')
    if Resposta.proxima_campanha == None:
        return render(request, 'pesquisa.html', {'campanha': campanha, 'perguntas': perguntas, 'email': email,})
"""

def detalhes_campanha(request, campanha_id, email):
    email = decrypt_email(email)
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    perguntas = Pergunta.objects.filter(pergunta_campanha=campanha).prefetch_related('respostas')
    
    # Adicionar lógica para verificar se alguma resposta direciona para outra campanha
    tem_proxima_campanha = False
    for pergunta in perguntas:
        for resposta in pergunta.respostas.all():
            if resposta.proxima_campanha is not None:
                tem_proxima_campanha = True
                break
        if tem_proxima_campanha:
            break

    return render(request, 'pesquisa.html', {'campanha': campanha, 'perguntas': perguntas, 'email': email, 'tem_proxima_campanha': tem_proxima_campanha})


def sucesso_campanha(request, campanha_id, email):
    #email_decrypted = decrypt_email(email)  # Assume-se que esta função está funcionando corretamente
    email = encrypt_email(email)
    campanha = get_object_or_404(Campanha, pk=campanha_id)
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('resposta_'):
                pergunta_id = key.split('_')[-1]
                resposta_id = value
                resposta = Resposta.objects.get(pk=resposta_id)

                # Se a resposta leva a uma próxima campanha, recriptografe o e-mail antes do redirecionamento
                if resposta.proxima_campanha:
                    nova_campanha_id = resposta.proxima_campanha.id
                    # email_encrypted = encrypt_email(email_decrypted)  # Recriptografa o e-mail
                    return HttpResponseRedirect(reverse('perguntas_respostas', args=(nova_campanha_id, email)))

                to_save_email = decrypt_email(email)
                RespostaUsuario.objects.create(
                    email=to_save_email,
                    campanha=campanha,
                    pergunta_id=pergunta_id,
                    resposta_texto=resposta.resposta_texto
                )

        # Após processar todas as respostas, redirecione para a página de conclusão, recriptografando o e-mail
        # email_encrypted = encrypt_email(email_decrypted)
        email = encrypt_email(email)
        return render(request, 'fim_pesquisa.html', {'campanha': campanha_id, 'email': email})



"""
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
                encrypt_mail = encrypt_email(email)

    return render(request, 'fim_pesquisa.html', {'campanha': campanha_id, 'email': encrypt_mail})
"""