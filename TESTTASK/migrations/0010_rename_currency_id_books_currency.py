# Generated by Django 4.0.4 on 2022-05-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TESTTASK', '0009_books_currency_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='currency_id',
            new_name='currency',
        ),
    ]