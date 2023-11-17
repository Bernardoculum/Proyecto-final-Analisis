# Generated by Django 4.2.5 on 2023-09-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion_app', '0002_authuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(db_column='ID_categoria', primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Nombre_categoria', max_length=50)),
                ('descripcion', models.CharField(blank=True, db_collation='Modern_Spanish_CI_AS', db_column='Descripcion', max_length=100, null=True)),
                ('estado', models.BooleanField(db_column='Estado')),
            ],
            options={
                'db_table': 'Categorias',
                'managed': False,
            },
        ),
    ]