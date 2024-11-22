from django.db import models
from main_page.models import Books

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='orders')
    