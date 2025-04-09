from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name='Moderators')
        if created:
            self.stdout.write(self.style.SUCCESS('Группа Moderators создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа Moderators уже существует'))

        content_type = ContentType.objects.get_for_model(Product)

        permissions = Permission.objects.filter(content_type=content_type).filter(
            codename__in=[
                'change_product',
                'view_product',
                'change_product_is_published',
                'change_product_description',
                'change_product_category'
            ]
        )

        moderator_group.permissions.set(permissions)
