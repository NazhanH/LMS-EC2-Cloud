# your_app/management/commands/create_custom_groups.py

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

GROUPS_MODELS_PERMISSIONS = {
    'Librarians': {
        'book.Book': ['add', 'view', 'change', 'delete'],
        'book.BorrowList': ['view', 'delete', 'add', 'change'],
    },
    'Patrons': {
        'book.Book': ['view'],
        'book.BorrowList': ['view'],
    },
    # Add more groups, models, and permissions as needed
}

class Command(BaseCommand):
    help = 'Create custom groups and assign specific model permissions'

    def handle(self, *args, **options):
        for group_name, models_permissions in GROUPS_MODELS_PERMISSIONS.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for model_full_name, permissions_list in models_permissions.items():
                app_label, model_name = model_full_name.split('.')
                model = apps.get_model(app_label, model_name)
                content_type = ContentType.objects.get_for_model(model)
                
                for perm_name in permissions_list:
                    permission_codename = f'{perm_name}_{model_name.lower()}'
                    try:
                        permission = Permission.objects.get(content_type=content_type, codename=permission_codename)
                        group.permissions.add(permission)
                    except Permission.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Permission {permission_codename} does not exist for model {model_full_name}'))           
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created/updated group "{group_name}" and assigned specified permissions'))
        
        admin = User.objects.filter(is_superuser=True).first()
        if admin:
            admin_group = Group.objects.get(name='Librarians')
            admin.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS('Successfully added admin to Librarians group'))
        else:
            self.stdout.write(self.style.WARNING('No superuser found. Please create a superuser and run the command again'))



        



