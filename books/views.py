from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Category
from .forms import BookForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.urls import include


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect("book_index")
    return render(request, "books/homepage.html")


def book_index(request):
    books = Book.objects.all()
    return render(request, "books/book_index.html", {"books": books})


@login_required
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="home")
    return render(request, 'books/add_book.html', {"form": form})


def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/view_book.html', {"book": book})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookForm(instance=book)
    return render(
        request,
        'books/edit_book.html',
        {"form": form, "book": book}
    )


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to="home")
    return render(request, 'books/delete_book.html', {"book": book})


def add_category(request):
    if request == 'GET':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="home")
    return render(request, 'books/add_category.html', {'form': form})


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    return render(request, 'books/view_category.html', {"category": category, "books": books})
