from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

class BooksByGenre(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Book.objects.filter(genre__name=genre)

class BooksByAuthor(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        return Book.objects.filter(author__name=author)
