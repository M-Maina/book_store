from django.shortcuts import render, get_object_or_404


from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.htm", {"books":books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_outlet/book_detail.htm", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
        })