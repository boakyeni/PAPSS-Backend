# Generated by Django 4.2.7 on 2023-11-14 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_remove_product_web_id_alter_product_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="category",
            new_name="categories",
        ),
    ]
