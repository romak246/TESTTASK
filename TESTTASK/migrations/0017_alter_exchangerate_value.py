# Generated by Django 4.0.4 on 2022-05-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TESTTASK', '0016_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=19, verbose_name='Значение'),
        ),
    ]
