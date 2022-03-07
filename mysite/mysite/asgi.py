"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()


#protocoltype router will first inspect the type of connection
#if it is websocket, the connection will be given to AuthMiddleWareStack
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})

#AuthMiddleWareStack will populate the connection's scope with a 
#reference to the currently authenticated user
#similar to django's AuthenticationMiddleware for https connection

