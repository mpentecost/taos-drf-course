# Generated by Django 3.0.3 on 2020-02-27 21:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dealerships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealership',
            name='web_users',
            field=models.ManyToManyField(related_name='dealerships', to=settings.AUTH_USER_MODEL),
        ),
    ]
