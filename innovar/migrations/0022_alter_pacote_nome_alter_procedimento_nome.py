# Generated by Django 4.2.4 on 2023-08-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0021_delete_desconto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pacote",
            name="nome",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="procedimento",
            name="nome",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
