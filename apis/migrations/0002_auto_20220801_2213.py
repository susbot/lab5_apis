# Generated by Django 3.1.14 on 2022-08-01 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
