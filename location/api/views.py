from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegionSerializer, DistrictSerializer
from ..models import Region, District
from .permissions import IsAdminAuthorUserOrReadOnly, IsOwnerOrReadOnly


class RegionCreateApiView(generics.ListCreateAPIView):
    queryset = Region
    serializer_class = RegionSerializer


class RegionRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region
    serializer_class = RegionSerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class DistrictCreateApiView(generics.ListCreateAPIView):
    queryset = District
    serializer_class = DistrictSerializer


class DistrictRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District
    serializer_class = DistrictSerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]
