from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 12)

    def __str__(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length = 20)
    razaoSocial = models.CharField(max_length = 50)

    def __str__(self):
        return self.cpf + self.razaoSocial

class Autor(Pessoa):
    curriculo = models.CharField(max_length = 150)

    def __str__(self):
        return self.curriculo

class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    eventoPrincipal = models.TextField()
    sigla = models.CharField(max_length = 10)
    dataEHoraDeinicio = models.DateTimeField(blank = True, null = True)
    palavrasChave = models.IntegerField(max_length = 20)
    logotipo = models.IntegerField(max_length = 10)
    realizador = models.ForeignKey(Pessoa, related_name = 'Pessoa', null = True, blank = False)
    cidade = models.CharField(max_length = 20)
    uf = models.CharField(max_length = 2)
    endereco = models.CharField(max_length = 20)
    cep = models.CharField(max_length = 12)

    def __str__(self):
        return self.nome + self.eventoPrincipal

class EventoCientifico(Evento):
    issn = models.CharField(max_length = 100)

    def __str__(self):
        return self.issn

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length = 50)
    evento = models.ForeignKey(EventoCientifico, related_name = 'EventoCientifico', null = True, blank = False)
    Autores = models.ManyToManyField(Autor, blank = True)

    def __str__(self):
        return self.titulo
