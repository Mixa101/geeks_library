from django.db import models

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