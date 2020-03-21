# Generated by Django 2.2.10 on 2020-03-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Tipo de categoria',
                'verbose_name_plural': 'Tipos de Categorias',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('tipo_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categoria.TipoCategoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
