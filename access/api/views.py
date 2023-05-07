from rest_framework import generics, status
from rest_framework.response import Response

from ..models import User, role, userRole
from .serializers import RoleSerializers, UserRoleSerializers, UserSerializers
from .permissions import IsAdminAuthorUserOrReadOnly, IsOwnerOrReadOnly


class RoleCreateApiView(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializers


class RoleRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializers
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class UserRoleCreateApiView(generics.ListCreateAPIView):
    queryset = userRole.objects.all()
    serializer_class = UserRoleSerializers


class UserRoleRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = role.objects.all()
    serializer_class = UserRoleSerializers
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class UserCreateApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminAuthorUserOrReadOnly]
