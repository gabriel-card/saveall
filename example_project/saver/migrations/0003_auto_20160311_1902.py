# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saver', '0002_auto_20160311_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table02',
            old_name='nome_raca',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='table03',
            name='dono',
            field=models.ForeignKey(to='saver.Table01'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table03',
            name='raca',
            field=models.ForeignKey(to='saver.Table02'),
            preserve_default=True,
        ),
    ]
