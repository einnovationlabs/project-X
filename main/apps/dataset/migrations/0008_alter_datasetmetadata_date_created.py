# Generated by Django 4.2.3 on 2023-10-06 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0007_alter_datasetmetadata_resource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetmetadata',
            name='date_created',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
