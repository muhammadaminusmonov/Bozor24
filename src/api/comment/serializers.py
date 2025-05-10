from rest_framework import serializers
from comment.models import CommentProduct, CommentUser

class CommentProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommentProduct
        fields = ['id', 'user', 'product', 'text', 'writed_at', 'parent_comment']

class CommentUserSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CommentUser
        fields = ['id', 'seller']
