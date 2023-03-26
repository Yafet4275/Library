from django.urls import path
from .views import Home, crearAutor, listAutor, editAuthor

urlpatterns = [
    path('crear_autor/', crearAutor, name='crearAutor'),
    path('author_list/', listAutor, name='authorList'),
    path('autor_edit/<int:id>', editAuthor, name='authorEdit') 
]
