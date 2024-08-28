from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account_app import models

class user_register_form(UserCreationForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','birthday']

    def save(self,commit=True):
        user=super().save(commit=False)
        if commit:
            user.save()
            
            account_no=11000+user.id
            birthday = self.cleaned_data.get('birthday')
            models.Account.objects.create(user=user,account_no=account_no,birthday=birthday)
        return user
            
            
class Deposit_form(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ['balance']
        
    