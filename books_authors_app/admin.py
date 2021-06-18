from django.contrib import admin
from books_authors_app.models import Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)