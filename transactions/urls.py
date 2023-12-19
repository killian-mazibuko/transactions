"""Defines URL patterns for transactions."""
from django.conf.urls import url
from . import views
app_name = 'transactions'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all transactions.
    url(r'^transactions/$', views.transactions, name='transactions'),

    # Page for adding a new topic
    url(r'^new_transaction/$', views.new_transaction, name='new_transaction'),
]