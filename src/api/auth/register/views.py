from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            errors = serializer.errors
            if 'password' in errors:
                return Response({"message": "password is weak"}, status=422)
            if 'phone' in errors and "already exists" in str(errors['phone']):
                return Response({"message": "user already exist"}, status=409)
            return Response({"message": "bad request"}, status=400)

        try:
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "try again later"}, status=500)

    def get(self, request):
        user = request.user
        serializer = UserRegisterSerializer(user)
        return Response(serializer.data, status=200)
