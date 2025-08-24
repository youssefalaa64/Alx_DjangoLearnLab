# bookshelf/forms.py

from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search books', max_length=100)



class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Email')