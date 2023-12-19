from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'transaction_type']
        labels = {'transaction_type': 'Type (D/C) '}
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}
