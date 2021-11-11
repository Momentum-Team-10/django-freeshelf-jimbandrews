from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['created_at']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
