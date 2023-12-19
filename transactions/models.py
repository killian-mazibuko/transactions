from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    '''A topic the user is learning about'''
    transaction_type = models.CharField(max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self) -> str:
        ''' Return a string representation of the model'''
        return self.description[:50] + '...'
