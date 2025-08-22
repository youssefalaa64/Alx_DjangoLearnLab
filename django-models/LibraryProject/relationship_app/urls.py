from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns =[
path('book/', list_books, name='book-list'),
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail')


]