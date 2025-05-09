from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserLoginSerializer

User = get_user_model()

class LoginAPIView(APIView):
    def get_permissions(self):
        if self.request.method.lower() == 'post':
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "bad request"}, status=status.HTTP_400_BAD_REQUEST)

        phone = serializer.validated_data['phone']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(phone=phone)
            if not user.check_password(password):
                return Response({"message": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"message": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "try again later"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
