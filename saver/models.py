from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'pessoa'


class Raca(models.Model):
    nome_raca = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nome_raca

    class Meta:
        verbose_name = 'raca'


class Animal(models.Model):
    nome = models.CharField(max_length=30)
    dono = models.ForeignKey(Pessoa)
    raca = models.ForeignKey(Raca)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'animal'
