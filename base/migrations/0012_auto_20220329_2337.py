# Generated by Django 3.1.4 on 2022-03-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20220329_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='organizationName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
