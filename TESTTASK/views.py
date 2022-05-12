from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, mixins, generics
from .serializers import *
from .models import *


class BookAPIView(GenericAPIView):
    serializer_class = BookPostSerializer
    queryset = Books.objects.all()
    def get(self, request):

        """ Получить список книг"""
        authors = Books.objects.all()
        serializer = BookGetSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):

        """Создать книгу"""
        serializer = BookPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)





class BookOneAPIView(GenericAPIView):
    serializer_class = BookUpdateSerializer
    def get (self, request, book_id):
        """Получить книгу по id"""
        book = Books.objects.get(id=book_id)
        serializer = BookGetSerializer(book, many=False)
        return Response(serializer.data)


    def put(self, request, book_id):
        """ Редактировать книгу """
        book = Books.objects.get(id=book_id)
        serializer = BookUpdateSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        """Удалить книгу"""
        book = Books.objects.get(id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreAPIView(APIView):

    def get (self, request):
        """Получить все жанры"""
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)


    def post(self, post):
        """Создать жанр"""
        serializer_post = GenreSerializer(data=post.data)
        if serializer_post.is_valid():
            serializer_post.save()
        return Response(serializer_post.data, status=status.HTTP_201_CREATED)


class GenreOneAPIView(APIView):

     def get (self, request, genre_id):
        """Получить жанр по id"""
        genre = Genre.objects.get(id=genre_id)
        get_book = GenreSerializer(genre)
        return Response(get_book.data)


     def put(self, request, genre_id):
        """Изменить жанр"""
        genre = Genre.objects.get(id=genre_id)
        put_book = GenreSerializer(genre, data=request.data)
        if put_book.is_valid(raise_exception=True):
            put_book.save()
            return Response(put_book.data)
        return Response(put_book.data, 'govno')

     def delete(self, request, genre_id):
        """Удалить жанр"""
        genre = Genre.objects.get(id=genre_id)
        genre.delete()
        return Response("удалено")


class CurrencyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """ Получить список валют"""
        genre = CurrencyName.objects.all()
        serializer = CurrencySerializer(genre, many=True)
        return Response(serializer.data)

    def post(self, post):
        """ Запостить валюту"""
        serializer_post = CurrencyPostSerializer(data=post.data)
        if serializer_post.is_valid():
            serializer_post.save()
        return Response(serializer_post.data, status=status.HTTP_201_CREATED)



class CurrencyOneAPIView(APIView):
    """ Получить валюту по id"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cur_id):

        genre = CurrencyName.objects.get(id=cur_id)
        get_book = CurrencySerializer(genre)
        return Response(get_book.data)

    def put(self, request, cur_id):
        """Редактировать валюту"""
        currency = CurrencyName.objects.get(id=cur_id)
        put_currency = CurrencySerializer(currency, data=request.data)
        if put_currency.is_valid(raise_exception=True):
            put_currency.save()
            return Response(put_currency.data)
        return Response(put_currency.data, 'govno')

    def delete(self, request, cur_id):
        """Удалить валюту"""
        currency = CurrencyName.objects.get(id=cur_id)
        currency.delete()
        return Response("удалено")

class UserRegisterAPIView(GenericAPIView):
    serializer_class = UserRegister
    def post(self, post):
        """Регистрация"""
        serializer_post = UserRegister(data=post.data)
        if serializer_post.is_valid(raise_exception=True):
            serializer_post.save()
        return Response(serializer_post.data, status=status.HTTP_201_CREATED)
