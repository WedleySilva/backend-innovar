# Generated by Django 4.2.4 on 2023-08-14 19:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0004_alter_usuariocustomizado_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cliente",
            name="cpf",
        ),
        migrations.RemoveField(
            model_name="cliente",
            name="numero_telefone",
        ),
    ]
