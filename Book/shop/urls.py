from django.urls import path
from .views import BookList, BookDetail, BooksByGenre, BooksByAuthor

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<slug:slug>/', BookDetail.as_view(), name='book-detail'),
    path('books/genre/<str:genre>/', BooksByGenre.as_view(), name='books-by-genre'),
    path('books/author/<str:author>/', BooksByAuthor.as_view(), name='books-by-author'),
]
