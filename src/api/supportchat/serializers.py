from rest_framework import serializers
from supportchat.models import SupportChatRoom, SupportMessage

class SupportMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = SupportMessage
        fields = ['id', 'room', 'sender', 'sender_username', 'message', 'sent_at']
        read_only_fields = ['id', 'sender', 'sent_at', 'sender_username', 'room']


class SupportChatRoomSerializer(serializers.ModelSerializer):
    messages = SupportMessageSerializer(many=True, read_only=True)

    class Meta:
        model = SupportChatRoom
        fields = ['id', 'user', 'created_at', 'messages']
        read_only_fields = ['id', 'created_at', 'user']
