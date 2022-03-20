# Generated by Django 4.0.3 on 2022-03-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='zipCode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(verbose_name='date created'),
        ),
    ]
