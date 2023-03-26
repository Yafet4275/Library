from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import Autorform
from .models import Autor

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
    autores = Autor.objects.all()
    print(autores)
    return render(request,'libros/autor_list.html',{'autores': autores})

def editAuthor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id = id)          #Get is for only one result, when I need information is used method GET, when submit is POST method
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
    