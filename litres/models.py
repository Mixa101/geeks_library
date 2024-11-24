from django.db import models

class LitresModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img = models.ImageField()
    
    def __str__(self):
        return self.name