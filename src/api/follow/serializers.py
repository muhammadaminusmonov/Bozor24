from rest_framework import serializers
from user.models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'seller', 'follow_at']
        read_only_fields = ['follower', 'follow_at']
