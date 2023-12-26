from rest_framework import serializers
from .models import Book, Genre, Author

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre_name = serializers.ReadOnlyField(source='genre.name')
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['title', 'content', 'slug', 'genre', 'genre_name', 'image', 'date_published', 'author', 'author_name']

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()
