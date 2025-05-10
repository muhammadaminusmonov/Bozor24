from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework_simplejwt.tokens import UntypedToken


def validate_token(token):
    try:
        untyped_token = UntypedToken(token)
        if untyped_token.token_type == 'access':
            return AccessToken(token)
        elif untyped_token.token_type == 'refresh':
            return RefreshToken(token)
        else:
            raise TokenError('Invalid token type')

    except TokenError as e:
        raise TokenError(f'Invalid token: {str(e)}')
class LoginWithAccessTokenView(APIView):
    def post(self, request):
        token_str = request.headers.get("Authorization")

        if not token_str or not token_str.startswith("Bearer "):
            return Response({"detail": "Token required"}, status=400)

        token_str = token_str.split(" ")[1]

        try:
            access_token = AccessToken(token_str)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)

            refresh = RefreshToken.for_user(user)

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=200)

        except TokenError:
            return Response({"detail": "Invalid or expired token"}, status=400)
        except Exception:
            return Response({"detail": "try again later"}, status=500)


class RefreshAccessTokenView(APIView):
    def post(self, request):
        token_str = request.data.get("refresh")

        if not token_str:
            return Response({"detail": "Refresh token required"}, status=400)

        try:
            refresh_token = RefreshToken(token_str)
            return Response({
                "access": str(refresh_token.access_token),
                "refresh": str(refresh_token),
            }, status=200)

        except TokenError:
            return Response({"detail": "Invalid or expired refresh token"}, status=400)
        except Exception:
            return Response({"detail": "try again later"}, status=500)
