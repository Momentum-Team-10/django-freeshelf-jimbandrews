from django.shortcuts import get_object_or_404, render, redirect
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


def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/view_book.html', {"book": book})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to="book_index")
    return render(request, 'books/edit_book.html', {"form": form, "book": book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to="book_index")
    return render(request, 'books/delete_book.html', {"book": book})
