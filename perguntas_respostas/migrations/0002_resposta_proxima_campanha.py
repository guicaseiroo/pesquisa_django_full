# Generated by Django 5.0.4 on 2024-04-11 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0003_campanha_campanha_fundo'),
        ('perguntas_respostas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='proxima_campanha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proxima_campanha', to='campanhas.campanha'),
        ),
    ]
