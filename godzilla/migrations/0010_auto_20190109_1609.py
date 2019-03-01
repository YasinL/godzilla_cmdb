# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-09 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godzilla', '0009_auto_20190108_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='tenginehost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.GenericIPAddressField()),
                ('hostredisport', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='recordlogtable',
            name='logtime',
            field=models.DateTimeField(default='2019-01-09 16:09:20'),
        ),
    ]