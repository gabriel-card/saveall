from django.db import models


class Table01(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table01'


class Table02(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table02'


class Table03(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dono = models.ForeignKey(Table01)
    raca = models.ForeignKey(Table02)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table03'
