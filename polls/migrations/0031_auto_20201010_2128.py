# Generated by Django 2.2 on 2020-10-10 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_auto_20201010_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Poll'),
        ),
    ]
