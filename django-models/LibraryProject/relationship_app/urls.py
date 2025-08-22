from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views

urlpatterns =[
path('book/', list_books, name='book-list'),
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
path('register/', views.register_view, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),


]