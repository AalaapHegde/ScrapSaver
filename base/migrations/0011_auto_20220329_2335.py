# Generated by Django 3.1.4 on 2022-03-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20220329_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]