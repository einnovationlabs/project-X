# Generated by Django 4.2.3 on 2023-08-18 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('dataset', '0004_dataset_comment_user_dataset_like_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dataset.dataset')),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dataset.like')),
            ],
        ),
        migrations.CreateModel(
            name='User_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dataset.like')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Dataset_Like_User',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='likes',
            field=models.ManyToManyField(through='dataset.Dataset_Like', to='dataset.like'),
        ),
    ]
