# Generated by Django 3.1.2 on 2021-02-09 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, default='-', max_length=100)),
                ('sex', models.CharField(blank=True, default='-', max_length=30)),
                ('age', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('education', models.CharField(blank=True, default='-', max_length=100)),
                ('group', models.CharField(blank=True, default='-', max_length=100)),
                ('city', models.CharField(blank=True, default='-', max_length=50)),
                ('street', models.CharField(blank=True, default='-', max_length=50)),
                ('move', models.CharField(blank=True, default='-', max_length=10)),
                ('phone', models.CharField(blank=True, default='-', max_length=20)),
                ('job_wish', models.CharField(blank=True, default='', max_length=300)),
                ('profession', models.CharField(blank=True, default='', max_length=300)),
                ('experience', models.CharField(blank=True, default='', max_length=300)),
                ('limits', models.CharField(blank=True, default='', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
