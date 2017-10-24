"""
Django management command definition.
"""

import os
import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    Set a super user based on environment variables.
    """

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)

        superuser_email = os.environ.get(
            'SUPERUSER_EMAIL'
        )
        superuser_password = os.environ.get(
            'SUPERUSER_PASSWORD',
            '#Default8'
        )

        if superuser_email:

            user = User.objects.filter(email=superuser_email)

            # Create the user if they don't exist
            if user:
                user = user.first()
            else:
                user = User.objects.create_user(
                    superuser_email,
                    superuser_email,
                    superuser_password
                )

            logging.info('Setting %s as a super user.', superuser_email)
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
            user.save()
