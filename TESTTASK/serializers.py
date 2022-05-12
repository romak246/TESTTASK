from datetime import date
from random import choice
from string import ascii_letters

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['Name', 'id']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyName
        fields = ['name', 'symbol']

class CurrencyPostSerializer(serializers.ModelSerializer):


    def create(self,  validated_data):
        print(validated_data["name"])

        currency_search = CurrencyName.objects.filter(name=validated_data["name"])
        print(currency_search)
        if currency_search.count() > 1:
            raise Exception('такая валюта уже существует')
        return super().create(validated_data)



    class Meta:

        model = CurrencyName
        fields = ['name', 'symbol']


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False, read_only=False)
    currency = CurrencySerializer(many=False, read_only=False)
    price = serializers.SerializerMethodField()



    class Meta:
        model = Books

        fields = ['title', 'genres', 'author', 'price', 'currency']


class BookGetSerializer(serializers.ModelSerializer):


    author = AuthorSerializer(many=False, read_only=False)
    rub_price = serializers.SerializerMethodField()


    def get_rub_price(self, instance):
        today = date.today()
        rub_price = ExchangeRate.objects.filter(at=today, base_id=instance.currency_id, quoted_id=1488).get()
        rub_exchange = rub_price.value
        final = instance.price*rub_exchange
        return final

    class Meta:
        model = Books

        fields = ['title', 'genres', 'author', 'rub_price']


class GenreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Genre
        fields = ['title']


class BookPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books

        fields = [ 'title','genres','author','price','currency']



class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['title','genres','author','currency','price']

    def update(self, instance, validated_data):
        today = date.today()
        instance.genres.clear()
        genres_data = validated_data.pop('genres')
        currency_data = validated_data.pop('currency')
        print(genres_data)#ИНФОРМАЦИИ О ВВЕДЕНЫХ В ПОЛЕ PUT ЖАНРАХ
        print(currency_data.id)  # ИНФОРМАЦИИ О ВВЕДЕНЫХ В ПОЛЕ PUT ЖАНРАХ
        instance = super(BookUpdateSerializer, self).update(instance, validated_data)
        print(instance.currency.id) #ОБЪЕКТ КНИГА
        if instance.currency.id == currency_data.id:
            ...
        else:
            convert_object = ExchangeRate.objects.filter(at=today, base_id=instance.currency.id, quoted_id=currency_data.id).get()

            instance.currency = currency_data

            current_price = instance.price
            print(current_price, convert_object.value)
            final_price = current_price * convert_object.value
            instance.price = final_price

        instance.save()
        for genre in genres_data:

            instance.genres.add(genre)

        return instance
#
class UserRegister(serializers.ModelSerializer):
    def create(self, validated_data):

        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    class Meta:
        model = User

        fields = ['username', 'password']
        extra_kwargs = {"password": {'write_only': True}}


