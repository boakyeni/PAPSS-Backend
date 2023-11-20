# Generated by Django 4.2.7 on 2023-11-09 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_company_category_company_country_company_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="registration_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="company",
            name="verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="contactperson",
            name="companies",
            field=models.ManyToManyField(blank=True, to="profiles.company"),
        ),
        migrations.AlterField(
            model_name="rep",
            name="date_of_birth",
            field=models.DateField(auto_now_add=True, verbose_name="Date of Birth"),
        ),
    ]
