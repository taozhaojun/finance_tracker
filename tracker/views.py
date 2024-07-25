from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction, Category, Goal
from .forms import TransactionForm, GoalForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction, Category, Goal
from .forms import TransactionForm, GoalForm
from django.db.models import Sum

import json

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    goals = Goal.objects.filter(user=request.user)

    income_transactions = transactions.filter(type='income')
    expense_transactions = transactions.filter(type='expense')

    income_categories = list(income_transactions.values_list('category__name', flat=True).distinct())
    income_data = [float(income_transactions.filter(category__name=category).aggregate(Sum('amount'))['amount__sum'] or 0) for category in income_categories]

    expense_categories = list(expense_transactions.values_list('category__name', flat=True).distinct())
    expense_data = [float(expense_transactions.filter(category__name=category).aggregate(Sum('amount'))['amount__sum'] or 0) for category in expense_categories]

    context = {
        'transactions': transactions,
        'goals': goals,
        'income_categories': json.dumps(income_categories),
        'income_data': json.dumps(income_data),
        'expense_categories': json.dumps(expense_categories),
        'expense_data': json.dumps(expense_data),
    }

    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'tracker/add_transaction.html', {'form': form})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'tracker/add_goal.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    template_name = 'tracker/login.html'



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})