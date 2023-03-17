# Generated by Django 4.1.7 on 2023-02-28 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_alter_autor_options_alter_autor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('autor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libros.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
