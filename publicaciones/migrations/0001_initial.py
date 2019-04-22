# Generated by Django 2.1.1 on 2019-04-22 03:43

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivosPublicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='catalogos/')),
            ],
            options={
                'verbose_name': 'Archivo para publicación',
                'verbose_name_plural': 'Archivos para las publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=250)),
                ('portada', sorl.thumbnail.fields.ImageField(upload_to='colecciones/')),
                ('sinopsis', models.TextField()),
                ('year', models.CharField(max_length=20, verbose_name='año')),
                ('autores', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.AddField(
            model_name='archivospublicaciones',
            name='catalogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicaciones'),
        ),
    ]
