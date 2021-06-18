from django.urls import path
from . import views

urlpatterns=[
    path("", views.index), #todos los libros
    path("authors", views.authors), #todos los autores
    path("addAuthor", views.addNewAuthor),
    path("author/<int:authorId>", views.showAuthor),
    path("books/<int:bookId>", views.showBook),
    path("addNewBook", views.addNewBook),
    path("books/deleteAuthor/<int:authorId>", views.deleteAuthor),
    path("author/deleteBook/<int:bookId>", views.deleteBook)
    
]