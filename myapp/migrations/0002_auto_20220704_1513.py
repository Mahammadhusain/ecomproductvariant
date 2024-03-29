# Generated by Django 3.1.13 on 2022-07-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product',
            field=models.ManyToManyField(to='myapp.ProductNameModel'),
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='tag',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tag',
            field=models.ManyToManyField(to='myapp.TagModel'),
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='weight',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='weight',
            field=models.ManyToManyField(to='myapp.WeightModel'),
        ),
    ]
