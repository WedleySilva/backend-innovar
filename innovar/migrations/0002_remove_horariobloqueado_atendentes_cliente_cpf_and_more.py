# Generated by Django 4.2.4 on 2023-08-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="horariobloqueado",
            name="atendentes",
        ),
        migrations.AddField(
            model_name="cliente",
            name="cpf",
            field=models.CharField(default=0, max_length=14, unique=True),
        ),
        migrations.AddField(
            model_name="cliente",
            name="numero_telefone",
            field=models.CharField(default=0, max_length=15),
        ),
    ]
