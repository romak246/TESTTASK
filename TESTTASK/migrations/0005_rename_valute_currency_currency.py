# Generated by Django 4.0.4 on 2022-04-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TESTTASK', '0004_valute_currency'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='valute_currency',
            new_name='Currency',
        ),
    ]