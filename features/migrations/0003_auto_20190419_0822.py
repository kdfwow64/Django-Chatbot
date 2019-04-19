# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20190407_0227'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=128, verbose_name='Session id')),
                ('bot_reply', models.TextField(blank=True, null=True, verbose_name='Bot Reply')),
                ('user_input', models.CharField(blank=True, max_length=256, null=True, verbose_name='User Input')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='features.User')),
            ],
        ),
        migrations.CreateModel(
            name='NoMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_message', models.TextField(blank=True, null=True, verbose_name='Bot Reply')),
                ('anything_else', models.TextField(blank=True, null=True, verbose_name='User Input')),
                ('session_id', models.CharField(max_length=128, verbose_name='Session id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='features.User')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='userattractionmetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
        migrations.AddField(
            model_name='usercitymetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
        migrations.AddField(
            model_name='usereventmetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
        migrations.AddField(
            model_name='usermessagemetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
        migrations.AddField(
            model_name='userplaygroundmetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
        migrations.AddField(
            model_name='usersourcemetric',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Session'),
        ),
    ]
