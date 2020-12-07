from django.shortcuts import render

from .models import Book, Author


def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {"books": books, "authors": authors}
    return render(request, "homepage.html", context)
