from django.urls import path
from .views import Home, crearAutor, listAutor, editarAutor

urlpatterns = [
    path('crear_autor/', crearAutor, name='crearAutor'),
    path('author_list/', listAutor, name='authorList'),
    path('autor_edit/<int:id>', editarAutor, name='authorEdit') 
]
