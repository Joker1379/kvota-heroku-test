# Generated by Django 3.1.2 on 2021-06-20 08:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210505_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='limits',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Речевые ограничения;', 'Речевые ограничения;'), ('Слабый слух;', 'Слабый слух;'), ('Нарушенная координация;', 'Нарушенная координация;')], max_length=57),
        ),
    ]