# Generated by Django 3.1.7 on 2021-02-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_users_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_info',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
