# bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search books', max_length=100)
