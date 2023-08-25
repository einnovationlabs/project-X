# Generated by Django 4.2.3 on 2023-07-31 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0004_remove_datasetmetadata_dataset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset_DatasetTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DatasetTag', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dataset.datasettag')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dataset.dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(through='dataset.Dataset_DatasetTag', to='dataset.datasettag'),
        ),
    ]