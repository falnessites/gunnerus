# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-28 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserver', '0025_auto_20170727_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailnotification',
            name='recipient',
            field=models.ManyToManyField(null=True, to='reserver.UserData'),
        ),
    ]