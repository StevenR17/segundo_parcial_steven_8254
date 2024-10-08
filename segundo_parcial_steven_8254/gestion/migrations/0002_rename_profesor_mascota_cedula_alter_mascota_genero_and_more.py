# Generated by Django 5.1.1 on 2024-09-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='profesor',
            new_name='cedula',
        ),
        migrations.AlterField(
            model_name='mascota',
            name='genero',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(max_length=50),
        ),
    ]
