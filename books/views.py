from django.shortcuts import render
from .models import Book


# Create your views here.
def book_index(request):
    books = Book.objects.all()
    return render(request, "books/book_index.html", {"books": books})
