from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from region.models import Region
from .serializers import RegionSerializer
from ..permissions import IsSeller, IsPlatformAdmin

from rest_framework.permissions import BasePermission

class IsPlatformAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff  # yoki custom admin field

class RegionListCreateView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsPlatformAdmin()]
        return [IsAuthenticatedOrReadOnly()]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class RegionRetrieveUpdateDeleteView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     generics.GenericAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticatedOrReadOnly | IsPlatformAdmin]
        return [IsAuthenticatedOrReadOnly()]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

