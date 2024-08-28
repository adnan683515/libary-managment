from django.shortcuts import render,redirect
from book_app.models import Book
from cetagory_app.models import Cetagory

def home(request,cetagory_slug=None):
    book_objs = Book.objects.all()
    cetagory_book = Cetagory.objects.all()
    
    if cetagory_slug is not None:
        slug = Cetagory.objects.get(slug=cetagory_slug)
        book_objs = Book.objects.filter(cetagory=slug)
    
    return render(request,'home.html',{'all_book':book_objs,'cetagory':cetagory_book})