from django import forms
from .models import Autor

class Autorform(forms.ModelForm):       #It can be from modelForm or Form, but there is a different
    class Meta:
        model=Autor
        fields=['nombre', 'apellidos', 'nacionalidad','description']