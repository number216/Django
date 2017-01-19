from django.contrib import admin
from data.models import Book, Shoe, Note, Size

class ShoesAdmin(admin.ModelAdmin):
    list_display = ('brand_model', 'picture', 'description', 'price')
admin.site.register(Shoe, ShoesAdmin)

class SizesAdmin(admin.ModelAdmin):
    list_display = ('shoeID', 'size')
admin.site.register(Size, SizesAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'publish_date')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
admin.site.register(Note, NoteAdmin)