from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            return Response("logged out successfully", status=205)
        except Exception as e:
            return Response("try again later", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
