# Generated by Django 5.0.6 on 2024-06-12 00:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cargo',
            field=models.CharField(choices=[('SUPERVISOR', 'Supervisor'), ('TRABAJADOR', 'Trabajador'), ('GERENTE', 'Gerente'), ('GERENTE_GENERAL', 'Gerente General')], max_length=20),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('gerente_general', models.ForeignKey(limit_choices_to={'cargo': 'GERENTE_GENERAL'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('gerente', models.ForeignKey(limit_choices_to={'cargo': 'GERENTE'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionusuario.division')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionusuario.area')),
                ('supervisor', models.ForeignKey(limit_choices_to={'cargo': 'SUPERVISOR'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionusuario.grupo')),
                ('trabajador', models.ForeignKey(limit_choices_to={'cargo': 'TRABAJADOR'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
