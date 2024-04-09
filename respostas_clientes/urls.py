from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('campanha/<int:campanha_id>/<str:email>', views.apresentacao_campanha, name='apresentacao'),
    path('campanha/questionario/<int:campanha_id>/<str:email>', views.detalhes_campanha, name='perguntas_respostas'),
    path('campanha/sucesso/<int:campanha_id>/<str:email>', views.sucesso_campanha, name='sucesso_campanha'),
    path('encrypt/', views.cript, name="cript")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
