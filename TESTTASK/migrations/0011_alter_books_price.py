# Generated by Django 4.0.4 on 2022-05-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TESTTASK', '0010_rename_currency_id_books_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Цена'),
        ),
    ]
