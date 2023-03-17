from django.urls import path
from .views import Home, crearAutor

urlpatterns = [
    path('crear_autor/',crearAutor, name='crear_autor')    
]
