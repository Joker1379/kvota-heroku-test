# Generated by Django 3.1.2 on 2021-07-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210620_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
