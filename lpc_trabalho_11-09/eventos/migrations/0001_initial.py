# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('eventoPrincipal', models.TextField()),
                ('sigla', models.CharField(max_length=10)),
                ('dataEHoraDeinicio', models.DateTimeField(blank=True, null=True)),
                ('palavrasChave', models.IntegerField(max_length=20)),
                ('logotipo', models.IntegerField(max_length=10)),
                ('cidade', models.CharField(max_length=20)),
                ('uf', models.CharField(max_length=2)),
                ('endereco', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('curriculo', models.CharField(max_length=150)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Evento')),
                ('issn', models.CharField(max_length=100)),
            ],
            bases=('eventos.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cpf', models.CharField(max_length=12)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cnpj', models.CharField(max_length=20)),
                ('razaoSocial', models.CharField(max_length=50)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pessoa', to='eventos.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='Autores',
            field=models.ManyToManyField(blank=True, to='eventos.Autor'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EventoCientifico', to='eventos.EventoCientifico'),
        ),
    ]
