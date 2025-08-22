from django.shortcuts import render
from .models import Book 
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView
# create ur views here

def list_books(request) :
    Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'


