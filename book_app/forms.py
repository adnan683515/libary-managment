from book_app.models import comment
from django import forms

class commentFormBook(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','body','Rating']