# Generated by Django 4.2.3 on 2023-07-31 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0002_remove_datasetaddtfile_datasetfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='owner_organization',
        ),
    ]