import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from menu_app.utils import logger

User = get_user_model()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", default="admin")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", default="admin@mail.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", default="admin")


class Command(BaseCommand):
    name = "SUPERUSER"

    def handle(self, *args, **options):
        User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
        logger.debug(User.objects.filter(username=ADMIN_USERNAME))
