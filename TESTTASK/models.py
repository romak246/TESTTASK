from django.db import models


class Genre(models.Model):
    title = models.CharField('Название',max_length=100)

    def __str__(self):
        return self.title


class Author(models.Model):
    fieldname = 'myCharField'
    Name = models.CharField('Автор',max_length=100)
    def __str__(self):
        return 'Автор: ' + self.Name



class Currency(models.Model):
    today = models.DateField('Дата')
    usd_price = models.FloatField('Курс доллара')
    jpy_price = models.FloatField('Курс йены')
    eur_price = models.FloatField('Курс евро')


class CurrencyName(models.Model):
    name = models.CharField('Название валюты',max_length=100)
    symbol = models.CharField('Символ',max_length=1)
    def __str__(self):
        return 'Валюта: ' + self.name


class ExchangeRate(models.Model):
    base = models.ForeignKey(CurrencyName, on_delete=models.CASCADE, related_name='base')
    quoted = models.ForeignKey(CurrencyName, on_delete=models.CASCADE,related_name='quoted')
    at = models.DateField('На дату')
    value = models.DecimalField('Значение', max_digits=19, decimal_places=3)


class Books(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, blank=True)
    price = models.DecimalField('Цена', null=True,max_digits=19, decimal_places=2,blank=True)
    currency = models.ForeignKey(CurrencyName, on_delete=models.CASCADE, related_name='currency', null=True)
#
# class User(models.Model):
#
#
#
#     username = models.CharField('Имя пользователя', max_length=100)
#     password = models.CharField('Пароль', max_length=100)
#     key = models.CharField('Токен', max_length=100, null=True)