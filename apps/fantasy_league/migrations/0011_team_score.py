# Generated by Django 2.2.6 on 2020-01-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_league', '0010_auto_20200101_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]