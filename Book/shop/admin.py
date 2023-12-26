from django.contrib import admin
from .models import Book, Genre, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'author', 'date_published')
    search_fields = ('title', 'genre__name', 'author__name')
    prepopulated_fields = {'slug': ('title',)}

    
admin.site.register([Genre, Author])
