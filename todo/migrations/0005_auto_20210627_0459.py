# Generated by Django 3.2.4 on 2021-06-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_category_cat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
