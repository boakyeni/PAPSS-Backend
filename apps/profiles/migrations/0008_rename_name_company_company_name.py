# Generated by Django 4.2.7 on 2023-11-14 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0007_company_company_phone"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="name",
            new_name="company_name",
        ),
    ]
