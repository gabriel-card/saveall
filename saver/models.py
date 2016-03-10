from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'pessoa'


class Raca(models.Model):
    nome_raca = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome_raca

    class Meta:
        verbose_name = 'raca'


class Animal(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dono = models.ForeignKey(Pessoa)
    raca = models.ForeignKey(Raca)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'animal'
