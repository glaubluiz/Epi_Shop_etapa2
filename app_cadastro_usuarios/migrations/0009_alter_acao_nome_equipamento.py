# Generated by Django 4.2.16 on 2024-10-19 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0008_acao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='nome_equipamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cadastro_usuarios.epis'),
        ),
    ]
