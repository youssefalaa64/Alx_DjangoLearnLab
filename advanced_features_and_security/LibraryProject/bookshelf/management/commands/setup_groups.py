from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Set up groups and assign permissions'

    def handle(self, *args, **kwargs):
        book_model = apps.get_model('bookshelf', 'Book')
        permissions = Permission.objects.filter(content_type__app_label='bookshelf', content_type__model='book')

        perms = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_edit', 'can_create'],
            'Admins': ['can_view', 'can_edit', 'can_create', 'can_delete']
        }

        for group_name, perm_codenames in perms.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            for codename in perm_codenames:
                perm = permissions.get(codename=codename)
                group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))
