# Generated by Django 2.2 on 2020-10-06 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_choice_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='user_votes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
