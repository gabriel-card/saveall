from django.db import models


class Table_01(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table_01'


class Table_02(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table_02'


class Table_03(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rel1 = models.ForeignKey(Table_01)
    rel2 = models.ForeignKey(Table_02)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table_03'


class Table_04(models.Model):
    nome = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'table_03'
