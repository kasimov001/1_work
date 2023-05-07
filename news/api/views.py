from rest_framework import generics, status
from .serializers import NewSerializers
from ..models import News
from .permissions import IsAdminAuthorUserOrReadOnly


class NewCreateApiView(generics.ListCreateAPIView):
    queryset = News
    serializer_class = NewSerializers


class NewRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News
    serializer_class = NewSerializers
    permission_classes = [IsAdminAuthorUserOrReadOnly]