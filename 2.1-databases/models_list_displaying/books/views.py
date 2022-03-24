
from django.shortcuts import render, redirect

from .models import Book

def index(request):
    return redirect('books')

def books_view(request, dt = None):
    template = 'books/books_list.html'
    prev_page = None
    next_page = None
    book = Book.objects.all()
    date_list = [books.pub_date.strftime('%Y-%m-%d') for books in book]
    if dt:
        book = Book.objects.filter(pub_date=dt)
        index = date_list.index(dt)
        if index != 0:
            prev_page = date_list[index-1]
        if index != len(date_list)-1:
            next_page = date_list[index+1]
        context = {
            'books': book,
            'pub_date': dt,
            'prev_page': prev_page,
            'next_page': next_page,
        }


    else:
        book = Book.objects.all()
        context = {
            'books': book
        }
    return render(request, template, context)


