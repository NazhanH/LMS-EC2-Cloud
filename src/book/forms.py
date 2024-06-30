from datetime import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Book, BorrowList

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowBookForm(ModelForm):
    class Meta:
        model = BorrowList
        fields = '__all__'
        exclude = ['return_date', 'fine']
        widgets = {
            'expected_return_date': forms.DateInput(attrs={'type': 'date'})
        }

class ReturnBookForm(ModelForm):
    class Meta:
        model = BorrowList
        fields = ['book', 'borrower', 'return_date']
        exclude = ['fine']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'})
        }
