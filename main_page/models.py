from django.db import models
from django.conf import settings

class Books(models.Model):
    GENRE_CHOICES = [
        ('Fantastic', 'Фантастика'),
        ('Adventure', 'Приключения'),
        ('Science', 'Научная')
    ]
    book_name = models.CharField(max_length=255, verbose_name="Название книги")
    book_description = models.CharField(max_length=600, verbose_name="Краткое описание")
    book_price = models.PositiveIntegerField(verbose_name="сколько стоит книга?")
    book_release = models.DateField(verbose_name="Дата выхода")
    book_genre = models.CharField(max_length=255, verbose_name="Жанр книги", choices=GENRE_CHOICES)
    authors_email = models.EmailField(verbose_name="почта автора")
    authors_name = models.CharField(max_length=255, verbose_name="Имя автора")
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
class Comment(models.Model):
    RATES = ((i, i) for i in range(0, 11))
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(null=True)
    name = models.CharField(max_length=255,null=True)
    rate = models.IntegerField(null=True, choices=RATES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def rate_with_default(self):
        return self.rate or 1