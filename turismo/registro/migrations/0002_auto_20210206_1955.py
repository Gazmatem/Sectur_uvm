# Generated by Django 3.1.6 on 2021-02-06 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='antiguedad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empresa',
            name='entidad',
            field=models.CharField(default='active', max_length=50),
        ),
        migrations.AddField(
            model_name='empresa',
            name='fs_global',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empresa',
            name='giro',
            field=models.CharField(default='active', max_length=500),
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.CharField(default='active', max_length=50),
        ),
        migrations.AddField(
            model_name='empresa',
            name='razon_social',
            field=models.CharField(default='active', max_length=500),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sitio_fisico',
            field=models.CharField(default='active', max_length=500),
        ),
        migrations.AddField(
            model_name='empresa',
            name='tamano',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empresa',
            name='utilidades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='Estudiante', max_length=50),
        ),
        migrations.CreateModel(
            name='EvaluacionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(default='active', max_length=500)),
                ('puntaje', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.empresa')),
            ],
            options={
                'verbose_name': 'EvaluacionEmpresa',
                'verbose_name_plural': 'EvaluacionEmpresa',
                'db_table': 'EvaluacionEmpresa',
            },
        ),
    ]
