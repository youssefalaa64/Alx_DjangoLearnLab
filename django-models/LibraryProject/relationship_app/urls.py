from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
path('book/', list_books, name='book-list'),
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
path('register/', views.register_view, name='register'),
path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),


]