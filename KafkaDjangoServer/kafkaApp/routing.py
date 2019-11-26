from django.urls import re_path

from . import consumer,consumers,pubsub


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/consume/$',consumer.ChatConsumer),
    re_path(r'ws/pubsub/$',pubsub.ChatConsumer)
]

