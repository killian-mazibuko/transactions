from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


def index(request):
    """The home page for Transactions"""
    return render(request, 'transactions/index.html')

@login_required
def transactions(request):
    """Show all transactions."""
    transactions = Transaction.objects.filter(owner=request.user).order_by('date_added')
    debitTotal = Transaction.objects.filter(transaction_type='D').aggregate(Sum('amount'))
    creditTotal = Transaction.objects.filter(transaction_type='C').aggregate(Sum('amount'))   
    balance = debitTotal['amount__sum'] - creditTotal['amount__sum']
    context = {'transactions': transactions, 'balance': balance}
    return render(request, 'transactions/transactions.html', context)

@login_required
def new_transaction(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TransactionForm()
    else:
        # POST data submitted; process data.
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.owner = request.user
            new_transaction.save()
            return HttpResponseRedirect(reverse('transactions:transactions'))
    context = {'form': form}
    return render(request, 'transactions/new_transaction.html', context)