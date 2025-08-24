from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    search_fields = ('title', 'author')                     
    list_filter = ('publication_year',)                      


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Info"), {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ["username", "email", "first_name", "last_name", "is_staff", "date_of_birth"]
    search_fields = ["username", "email"]
