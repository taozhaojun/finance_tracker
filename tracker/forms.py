from django import forms
from .models import Transaction, Goal
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Transaction
        fields = ['type', 'category', 'amount', 'date', 'description']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'current_amount', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']