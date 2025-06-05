# book/models.py

from django.db import models

class Book(models.Model):
    judul = models.CharField(max_length=200)
    tahun_terbit = models.IntegerField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.judul
