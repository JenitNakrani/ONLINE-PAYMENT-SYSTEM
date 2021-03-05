# Generated by Django 3.1.5 on 2021-03-04 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('acno', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('balance', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]