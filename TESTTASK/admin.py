from django.contrib import admin


from.models import *

class AuthorAdmin(admin.ModelAdmin):
    def author_post_count(self, obj):
        return obj.post_set.count()
    author_post_count.short_description = "Количество"
list_display = ['author', 'author_post_count']


class BooksAdmin(admin.ModelAdmin):


    list_display = ['title', 'author', 'price', 'currency_id']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'user_field')

    def user_field(self, obj):
        return obj.books.all().count()


    user_field.short_description = 'userShort'





admin.site.register(Author, AuthorAdmin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Genre)
admin.site.register(Currency)
admin.site.register(CurrencyName)
admin.site.register(ExchangeRate)
