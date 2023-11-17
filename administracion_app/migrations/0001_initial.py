# Generated by Django 4.2.5 on 2023-09-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id_marcas', models.AutoField(db_column='ID_marcas', primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='Nombre_marca', max_length=80)),
                ('estado', models.BooleanField(db_column='Estado')),
                ('descripcion', models.CharField(blank=True, db_collation='Modern_Spanish_CI_AS', db_column='Descripcion', max_length=150, null=True)),
            ],
            options={
                'db_table': 'Marcas',
                'managed': False,
            },
        ),
    ]
