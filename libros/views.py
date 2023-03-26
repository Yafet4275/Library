from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import Autorform
from .models import Author

def Home(request):
    return render(request,'index.html')

def crearAutor(request):
    if request.method == 'POST':
        print(request.POST)
        autor_form = Autorform(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form=Autorform()
    return render(request,'libros/crear_autor.html',{'autor_form':autor_form})

def listAutor(request):
    autores = Author.objects.all()
    print(autores)
    return render(request,'libros/autor_list.html',{'autores': autores})

def editAuthor(request, id):
    autor_form = None
    error = None
    try:
        autor = Author.objects.get(id = id)          #Get is for only one result, when I need information is used method GET, when submit is POST method
        if request.method == 'GET':
            autor_form = Autorform(instance = autor)
        else:
            autor_form = Autorform(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = "It doesn't exist"                  #Manage the error when user doesn't exist
    return render(request, 'libros/crear_autor.html',{'autor_form':autor_form, 'error':error})

def deleteAuthor(request, id):                      #Permanent delete from data base 
    author = Author.objects.filter(status = True)             #Get author to be deleted
    if request.method == 'POST':
        author.delete()
        return redirect('authorList')
    return render(request, 'libros/author_delete.html',{'author':author})

# def deleteAuthor(request, id):                      #Permanent delete from data base 
#     author = Author.objects.get(id = id)             #Get author to be deleted
#     if request.method == 'POST':
#         author.delete()
#         return redirect('authorList')
#     return render(request, 'libros/author_delete.html',{'author':author})
    
