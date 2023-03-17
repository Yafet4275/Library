from django.shortcuts import render, redirect
from .forms import Autorform

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
