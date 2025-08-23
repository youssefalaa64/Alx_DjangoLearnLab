from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
# Create your models here





class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

def __str__(self):
    return self.name

class UserProfile(models.Model):
    ROLE_CHOICES= [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return f"{self.user.username} - {self.role}"

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
    
class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='bookshelf_user_set',  # or 'relationship_app_user_set' in the other model
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bookshelf_user_permissions',  # or 'relationship_app_user_permissions'
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )