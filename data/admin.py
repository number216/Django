from django.contrib import admin
from data.models import Book
from data.models import Shoe


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'price', 'stock', 'year')
admin.site.register(Book, AuthorAdmin)

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'description', 'size', 'price')
admin.site.register(Shoe, ShoesAdmin)