# Generated by Django 4.2.4 on 2023-08-22 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("innovar", "0019_alter_desconto_tipo_desconto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="desconto",
            name="cliente",
            field=models.ForeignKey(
                limit_choices_to={"eh_cliente": True},
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]