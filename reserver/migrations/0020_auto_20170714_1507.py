# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 13:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserver', '0019_merge_20170710_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='cruise',
            old_name='cruise_approved',
            new_name='is_approved',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userdata', to=settings.AUTH_USER_MODEL),
        ),
    ]
