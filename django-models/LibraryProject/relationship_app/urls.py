from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view

urlpatterns =[
path('book/', list_books, name='book-list'),
path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
path('register/', views.register_view, name='register'),
path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
path('admin-dashboard/', admin_view, name='admin_view'),
path('librarian-dashboard/', librarian_view, name='librarian_view'),
path('member-dashboard/', member_view, name='member_view'),


]