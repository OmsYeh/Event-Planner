# Generated by Django 3.1.7 on 2021-04-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Emaillist',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
