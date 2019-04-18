# Generated by Django 2.1.1 on 2019-04-18 02:51

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivosMemorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='memorias/')),
            ],
            options={
                'verbose_name': 'Archivo para Memoria',
                'verbose_name_plural': 'Archivos para las Memorias',
            },
        ),
        migrations.CreateModel(
            name='Memorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portada', sorl.thumbnail.fields.ImageField(upload_to='portadas/')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Memorias',
            },
        ),
        migrations.AddField(
            model_name='archivosmemorias',
            name='catalogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memorias.Memorias'),
        ),
    ]
