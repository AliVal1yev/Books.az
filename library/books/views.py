from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book



def books(request):
    books = Book.objects.all()
    template = loader.get_template('books/home.html')
    context = {
        'books': books
    }
    return HttpResponse(template.render(context, request))
