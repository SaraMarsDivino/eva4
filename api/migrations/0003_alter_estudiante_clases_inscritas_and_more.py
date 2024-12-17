# Generated by Django 5.0.7 on 2024-12-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_estudiante_clases_inscritas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='clases_inscritas',
            field=models.ManyToManyField(related_name='estudiantes', to='api.clase'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]