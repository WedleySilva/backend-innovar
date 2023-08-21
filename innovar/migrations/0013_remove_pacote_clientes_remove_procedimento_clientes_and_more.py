# Generated by Django 4.2.4 on 2023-08-21 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0012_pacote_clientes_procedimento_clientes_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pacote",
            name="clientes",
        ),
        migrations.RemoveField(
            model_name="procedimento",
            name="clientes",
        ),
        migrations.AlterField(
            model_name="clientepacote",
            name="cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pacotes_cliente",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="clientepacote",
            name="pacote",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clientes_pacote",
                to="innovar.pacote",
            ),
        ),
        migrations.AlterField(
            model_name="clientepacote",
            name="sessoes_total",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="clienteprocedimento",
            name="cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="procedimentos_cliente",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="clienteprocedimento",
            name="procedimento",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clientes_procedimento",
                to="innovar.procedimento",
            ),
        ),
        migrations.AlterField(
            model_name="clienteprocedimento",
            name="sessoes_total",
            field=models.PositiveIntegerField(default=0),
        ),
    ]