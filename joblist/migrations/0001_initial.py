# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=100)),
                ('jobdescription', models.TextField(max_length=300)),
                ('postdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
