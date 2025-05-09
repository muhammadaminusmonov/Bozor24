from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        if not phone or not password:
            raise serializers.ValidationError("Both phone number and password are required")

        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'phone', 'username', 'status']
        read_only_fields = ['id', 'phone', 'status']