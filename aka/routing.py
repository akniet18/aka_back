from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, include
from akaApp.consumers import CommentConsumer
from socket_token.socket_token import TokenAuthMiddlewareStack


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        TokenAuthMiddlewareStack(
        	URLRouter([
        		path('comments/', CommentConsumer)
        	])
        )
    ),
})