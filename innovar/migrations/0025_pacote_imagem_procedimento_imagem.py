# Generated by Django 4.2.6 on 2023-10-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0024_remove_usuariocustomizado_idade_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pacote",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="pacotes/"),
        ),
        migrations.AddField(
            model_name="procedimento",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="procedimentos/"),
        ),
    ]