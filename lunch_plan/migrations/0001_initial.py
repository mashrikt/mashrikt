# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 20:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work_week', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('will_have_lunch', models.BooleanField(default=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_week.Day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_lunch_days', models.ManyToManyField(to='work_week.Day')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]