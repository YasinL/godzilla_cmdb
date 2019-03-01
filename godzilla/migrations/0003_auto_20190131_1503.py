# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-31 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godzilla', '0002_auto_20190130_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaltool',
            name='varid',
        ),
        migrations.AlterField(
            model_name='globaltool',
            name='varname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='globaltool',
            name='varpath',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recordlogtable',
            name='logtime',
            field=models.DateTimeField(default='2019-01-31 15:03:07'),
        ),
    ]
