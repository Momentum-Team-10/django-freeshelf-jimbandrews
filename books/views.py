from django.shortcuts import render
from .models import Book
from .forms import BookForm


# Create your views here.
def book_index(request):
    books = Book.objects.all()
    return render(request, "books/book_index.html", {"books": books})


def add_book(request):
    if request == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="book_index")
    return render(request, 'books/add_book.html', {"form": form})


