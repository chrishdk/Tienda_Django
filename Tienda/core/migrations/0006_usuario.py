# Generated by Django 3.2.4 on 2021-06-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cuenta', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Codigo producto')),
            ],
        ),
    ]
