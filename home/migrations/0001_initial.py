# Generated by Django 4.0.4 on 2022-08-18 18:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque1peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=110)),
                ('quantidade_em_estoque', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('estoque_minimo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('obs', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque4peca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=120)),
                ('motorista', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('passageiro', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('assento_esquerdo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('assento_direito', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('quantidade_em_estoque', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('estoque_minimo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('obs', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('endereco', models.CharField(max_length=120)),
                ('complemento', models.CharField(max_length=120)),
                ('cep', models.CharField(max_length=12)),
                ('telefone', models.CharField(max_length=12)),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=128)),
                ('obs', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=128)),
                ('carro', models.CharField(max_length=128)),
                ('data_venda', models.DateTimeField(default=django.utils.timezone.now)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('venc_fatura', models.DateField(blank=True, null=True)),
                ('obs', models.TextField(max_length=100)),
                ('pag', models.CharField(choices=[('Em atendimento', 'Em atendimento'), ('A Vista', 'A Vista'), ('Pago', 'Pago'), ('A Prazo', 'A Prazo'), ('Orçamento', 'Orçamento'), ('Vencido', 'Vencido'), ('Parcelado 3X', 'Parcelado 3X')], max_length=20)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pessoa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='vendas',
            field=models.ManyToManyField(through='home.Venda', to='home.pessoa'),
        ),
    ]
