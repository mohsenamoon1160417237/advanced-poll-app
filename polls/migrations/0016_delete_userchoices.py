# Generated by Django 2.2 on 2020-10-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20201007_1341'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserChoices',
        ),
    ]
