from rest_framework import generics
from attribute.models import Attribute
from .serializers import AttributeSerializer
from api.permissions import IsOwnerOrReadOnly, IsPlatformAdmin, IsSeller
from rest_framework.permissions import AllowAny


class AttributeListCreateView(generics.ListCreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsPlatformAdmin()]
        else:
            return [AllowAny()]

class AttributeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
