# Generated by Django 4.2.4 on 2023-08-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0016_desconto"),
    ]

    operations = [
        migrations.AddField(
            model_name="desconto",
            name="cpf_superior",
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
