# Generated by Django 4.2.6 on 2023-10-17 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('horario', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descricao', models.TextField(blank=True)),
                ('vagas_disponiveis', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20)),
                ('placa', models.CharField(max_length=15)),
                ('capacidade', models.IntegerField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='main.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='InscricaoCarona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('A', 'Aceita'), ('R', 'Recusada')], max_length=1)),
                ('carona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carona')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='veiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcionarios', to='main.veiculo'),
        ),
        migrations.AddField(
            model_name='carona',
            name='motorista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caronas_oferecidas', to='main.funcionario'),
        ),
    ]