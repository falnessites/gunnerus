# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserver', '0004_merge_20170629_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cruise',
            name='season',
        ),
        migrations.AddField(
            model_name='cruiseday',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reserver.Season'),
        ),
        migrations.AlterField(
            model_name='cruise',
            name='cruise_owner',
            field=models.ManyToManyField(blank=True, related_name='cruise_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]