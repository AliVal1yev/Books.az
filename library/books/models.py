from django.db import models
from datetime import datetime

# Create your models here.

class Book(models.Model):
    name = models.CharField( max_length=50)
    price = models.FloatField()
    author_name = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', blank=True, upload_to='media/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name