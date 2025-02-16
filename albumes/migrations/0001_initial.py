# Generated by Django 5.1 on 2024-08-08 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('anio_lanzamiento', models.IntegerField()),
                ('genero', models.CharField(max_length=100)),
                ('portada', models.ImageField(upload_to='portadas/')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artistas.artista')),
            ],
        ),
    ]
