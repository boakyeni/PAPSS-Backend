# Generated by Django 4.2.7 on 2024-01-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_alter_product_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="currencyrates",
            name="tzs",
            field=models.FloatField(blank=True, default=1.0, null=True),
        ),
    ]