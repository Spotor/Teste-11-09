from django.contrib import admin
from eventos.models import *

admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
admin.site.register(Autor)


# Register your models here.
