# Generated by Django 2.2 on 2020-10-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20201007_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservotes',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
