# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saver', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Raca',
            new_name='Table01',
        ),
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='Table02',
        ),
        migrations.RenameModel(
            old_name='Animal',
            new_name='Table03',
        ),
        migrations.AlterModelOptions(
            name='table01',
            options={'verbose_name': 'table01'},
        ),
        migrations.AlterModelOptions(
            name='table02',
            options={'verbose_name': 'table02'},
        ),
        migrations.AlterModelOptions(
            name='table03',
            options={'verbose_name': 'table03'},
        ),
        migrations.RenameField(
            model_name='table01',
            old_name='nome_raca',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='table02',
            old_name='nome',
            new_name='nome_raca',
        ),
    ]
