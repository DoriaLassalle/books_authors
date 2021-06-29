from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


def index(request):
    allBooks=Book.objects.all()    
    context={
        "allbooks": allBooks
    }
    return render(request, "index.html", context)


def showBook(request, bookId):
    bookInfo=Book.objects.get(id=bookId)#traigo el objeto por el id que llega en la url
    title=bookInfo.title #extaigo del objeto lo que voy a utillizr y lo guardo en la variable
    desc=bookInfo.desc
    bookAuthors=bookInfo.authors.all()#traigo todos los autores de este libro(objeto)
    allAuthors=Author.objects.all()#traigo todos los autores (para el menu desplegable)

    context={
        "bookId": bookId,
        "title": title,
        "desc": desc,
        "bookAuthors":bookAuthors,
        "allAuthors": allAuthors
    }

    if request.method=='POST':
        chosenAuthor=request.POST["chooseAuthor"]
        bookInfo.authors.add(chosenAuthor)    #agrego un autor a este libro
    return render(request, "books.html", context)  


def addNewBook(request):
    newTitle=request.POST["title"] #guardo la info que viene del formulario
    newDesc=request.POST["desc"]
    Book.objects.create(title=newTitle, desc=newDesc)    #creo el nuevo objeto conla info recibida
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
    Author.objects.create(first_name=newName, last_name=newLastName, notes=newNote)# creo un nuevoonjeto conla info recibida del form
    return redirect("/authors")

def showAuthor(request, authorId):
    thisAuthor=Author.objects.get(id=authorId) #traigo el objeto por el id recibido en la url
    name=thisAuthor.first_name
    lastName=thisAuthor.last_name
    notes=thisAuthor.notes
    authorBooks=thisAuthor.books.all() #traigo los libros de este autor
    allBooks=Book.objects.all()#traigo todos los autores (para el menu desplegable)

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
        thisAuthor.books.add(chosenBook) #agrego un libro a este autor
    return render(request,"oneauthor.html", context)


def deleteAuthor(request, authorId):
    #authorToDelete=Author.objects.get(id=authorId)
    #currentBook=request.POST["bookId"]  #libro que se está mostrando      
    #authorToDelete.delete() #elimino el autor de la bd pero no el libro

    #eliminar solo la relacion
    authorToRemove=Author.objects.get(id=authorId)
    currentBook=request.POST["bookId"]
    authorToRemove.books.remove(currentBook) #elimino solo la relacionle quito el autor a este libro, no borro el autor
    
    return redirect(f"/books/{currentBook}") #reddirecciono al mismo libro donde estaba


def deleteBook(request, bookId):
    #bookToDelete=Book.objects.get(id=bookId)#recupero el libro a eliminar
    #currentAuthor=request.POST["authorId"]#guardo el autor que se esta mostrando para recargar el mismp  
    #bookToDelete.delete()  #borra de bd el libro
    
    #eliminar solo la relacion
    bookToRemove=Book.objects.get(id=bookId)#recupero el libro 
    currentAuthor=request.POST["authorId"]#guardo el autor 
    bookToRemove.authors.remove(currentAuthor)#elinimo solo la relacion

    return redirect(f"/author/{currentAuthor}")

   
    