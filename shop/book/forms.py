from django import forms
from .models import Book

class ProductForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['judul', 'tahun_terbit', 'author', 'genre', 'pages', 'price', 'description']