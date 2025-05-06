from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class UserLoginTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except InvalidToken as e:
            return Response({"detail": "Invalid or expired refresh token"},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Server error, try again later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
