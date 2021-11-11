from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'url',
            'cover_image',
            'description',
            'categories'
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
