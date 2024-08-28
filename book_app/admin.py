from django.contrib import admin
from book_app.models import Book,borrow_book,comment
# Register your models here.
admin.site.register(Book)
admin.site.register(borrow_book)
admin.site.register(comment)