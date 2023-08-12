"""
ASGI config for Send_and_get_Email_With_POST project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Send_and_get_Email_With_POST.settings')

application = get_asgi_application()
