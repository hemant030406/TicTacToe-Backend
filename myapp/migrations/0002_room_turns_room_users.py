# Generated by Django 5.0.3 on 2024-07-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='turns',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='room',
            name='users',
            field=models.JSONField(default=list),
        ),
    ]