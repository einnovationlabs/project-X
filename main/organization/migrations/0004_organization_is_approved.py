# Generated by Django 4.2.2 on 2023-08-16 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0003_rename_category_organization_categories_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
