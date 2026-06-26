from django import forms
from .models import User, Message

class UserForm(forms.ModelForm):
     class Meta:
         model = User
         fields = ['name', 'age', 'password']
         widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name.'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password.'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age.'}),
         }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message.', 'rows': 3})
        }
class MessageEditForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Edit your message.', 'rows': 3})
        }