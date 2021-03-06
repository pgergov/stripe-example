# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-06 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('magazine', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.Magazine'),
        ),
    ]
