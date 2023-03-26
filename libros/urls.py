from django.urls import path
from .views import Home, crearAutor, listAutor, editAuthor, deleteAuthor

urlpatterns = [
    path('author_list/', listAutor, name='authorList'),
    path('author_create/', crearAutor, name='authorCreate'),
    path('autor_edit/<int:id>', editAuthor, name='authorEdit'),
    path('author_delete/<int:id>', deleteAuthor, name='authorDelete') 
]
