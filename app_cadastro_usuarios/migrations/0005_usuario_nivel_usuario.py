# Generated by Django 4.2.16 on 2024-10-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0004_alter_epis_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nivel_usuario',
            field=models.CharField(choices=[('cliente', 'cliente'), ('administrador', 'administrador')], default='cliente', max_length=25),
        ),
    ]
