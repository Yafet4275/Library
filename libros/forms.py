from django import forms
from .models import Author

class Autorform(forms.ModelForm):       #It can be from modelForm or Form, but there is a different
    class Meta:
        model=Author
        fields=['nombre', 'apellidos', 'nacionalidad','description']