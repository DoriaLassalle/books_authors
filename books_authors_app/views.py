from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    allBooks=Book.objects.all()    
    context={
        "allbooks": allBooks
    }
    return render(request, "index.html", context)


def showBook(request, bookId):
    bookInfo=Book.objects.get(id=bookId)#objeto
    title=bookInfo.title
    desc=bookInfo.desc
    bookAuthors=bookInfo.authors.all()#consulto por el objeto
    allAuthors=Author.objects.all()

    context={
        "bookId": bookId,
        "title": title,
        "desc": desc,
        "bookAuthors":bookAuthors,
        "allAuthors": allAuthors
    }

    if request.method=='POST':
        chosenAuthor=request.POST["chooseAuthor"]
        bookInfo.authors.add(chosenAuthor)    
    return render(request, "books.html", context)


def addNewBook(request):
    newTitle=request.POST["title"]
    newDesc=request.POST["desc"]
    Book.objects.create(title=newTitle, desc=newDesc)    
    return redirect("/")


def authors(request):
    allAuthors=Author.objects.all() 

    context={
        "allAuthors": allAuthors
    }
    return render(request, "authors.html", context)


def addNewAuthor(request):
    newName=request.POST["firstName"]
    newLastName=request.POST["lastName"]
    newNote=request.POST["newNote"]
    Author.objects.create(first_name=newName, last_name=newLastName, notes=newNote)
    return redirect("/authors")

def showAuthor(request, authorId):
    thisAuthor=Author.objects.get(id=authorId)
    name=thisAuthor.first_name
    lastName=thisAuthor.last_name
    notes=thisAuthor.notes
    authorBooks=thisAuthor.books.all()
    allBooks=Book.objects.all()

    context={
        "authorId":authorId,
        "name":name,
        "lastName":lastName,
        "notes":notes,
        "authorBooks":authorBooks,
        "allBooks":allBooks
    }

    if request.method=='POST':
        chosenBook=request.POST["chooseBook"]
        thisAuthor.books.add(chosenBook)
    return render(request,"oneauthor.html", context)


def deleteAuthor(request, authorId):
    authorToDelete=Author.objects.get(id=authorId)
    for book in authorToDelete.books.all():
        bookId=book.id
    authorToDelete.delete() #elimino el autor del libro pero no el libro
    return redirect(f"/books/{bookId}")


def deleteBook(request, bookId):
    bookToDelete=Book.objects.get(id=bookId)#recupero el libro a eliminar
    for author in bookToDelete.authors.all(): #recorro su lista de autores  
        authorId=author.id                      
        #author.books.remove(bookToDelete) #elimina el libro para cada autor?...
        print(authorId)  
    bookToDelete.delete()  
    return redirect(f"/author/{authorId}")

   
    