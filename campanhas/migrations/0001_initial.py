# Generated by Django 5.0.4 on 2024-04-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campanha_nome', models.CharField(max_length=100)),
                ('campanha_descricao', models.TextField()),
                ('campanha_data_hora_validade', models.DateTimeField()),
            ],
        ),
    ]
