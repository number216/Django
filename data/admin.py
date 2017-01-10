from django.contrib import admin
from data.models import Book, Shoe, Note

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'price', 'stock', 'year')
admin.site.register(Book, AuthorAdmin)

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('brand_model', 'picture', 'description', 'size', 'price')
admin.site.register(Shoe, ShoesAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'publish_date')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
admin.site.register(Note, NoteAdmin)