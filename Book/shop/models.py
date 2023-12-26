from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, default='White Knight')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='books_images', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

    def __str__(self):
        return self.title
