"""
ASGI config for medicnewsblog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chatting.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicnewsblog.settings')
django.setup()

#Debugging
print("Django settings loaded: ",os.environ['DJANGO_SETTINGS_MODULE'])

application = ProtocolTypeRouter({
    "http:":get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            chatting.routing.websocket_urlpatterns
        )
    )
})
