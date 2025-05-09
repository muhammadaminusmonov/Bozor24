from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserLoginSerializer, UserProfileSerializer


class LoginAPIView(APIView):
    def get_permissions(self):
        if self.request.method.lower() == 'post':
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        print(serializer)
        if not serializer.is_valid():
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            phone=serializer.validated_data['phone_number'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"message": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
