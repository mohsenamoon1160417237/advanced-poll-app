# Generated by Django 2.2 on 2020-10-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_uservotes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uservotes',
            options={'verbose_name_plural': 'User votes'},
        ),
    ]
