# Generated by Django 4.1.1 on 2022-09-28 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_aluguel_funcionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departamento',
            },
        ),
        migrations.CreateModel(
            name='DepartamentoFuncionario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(db_column='id_departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='core.departamento')),
                ('funcionario', models.ForeignKey(db_column='id_funcionario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.funcionario')),
            ],
            options={
                'db_table': 'departamento_funcionario',
                'unique_together': {('departamento', 'funcionario')},
            },
        ),
    ]
