# Generated by Django 5.0.7 on 2024-07-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='id',
        ),
        migrations.AlterField(
            model_name='dish',
            name='dishId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dishName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='isPublished',
            field=models.BooleanField(default=False),
        ),
    ]
