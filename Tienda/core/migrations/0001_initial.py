# Generated by Django 3.2.4 on 2021-06-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cuenta', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='correo')),
                ('rut', models.CharField(max_length=50, verbose_name='rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
    ]
