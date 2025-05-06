from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'phone_number', 'password1', 'password2', 'username']
        extra_kwargs = {
            'username': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        try:
            validate_password(attrs['password1'])
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        if User.objects.filter(phone_number=attrs['phone_number']).exists():
            raise serializers.ValidationError({"phone_number": "User with this phone number already exists."})

        return attrs

    def create(self, validated_data):
        username = validated_data.get('username', f"user_{validated_data['phone_number']}")

        user = User.objects.create_user(
            username=username,
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            password=validated_data['password1'],
            status=1
        )

        return user