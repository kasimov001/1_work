from rest_framework import generics, status
from rest_framework.response import Response

from ..models import Contact, SocialLink, UserSocialLink
from .serializers import ContactSerializer, SocialLinkSerializer, UserSocialLinkSerializer
from .permissions import IsAdminAuthorUserOrReadOnly, IsOwnerOrReadOnly


class ContactCreateApiView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class SocialLinkCreateApiView(generics.ListCreateAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class SocialLinkRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]


class UserSocialLinkCreateApiView(generics.ListCreateAPIView):
    queryset = UserSocialLink.objects.all()
    serializer_class = UserSocialLinkSerializer


class UserSocialLinkRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSocialLink.objects.all()
    serializer_class = UserSocialLinkSerializer
    permission_classes = [IsAdminAuthorUserOrReadOnly]
