from django.urls import path
from .views import ContactCreateApiView, ContactRUDApiView, SocialLinkCreateApiView, SocialLinkRUDApiView,\
    UserSocialLinkCreateApiView, UserSocialLinkRUDApiView


urlpatterns = [
    path('contact-create/', ContactCreateApiView.as_view()),
    path('contact-rud/<int:pk>/', ContactRUDApiView.as_view()),
    path('social-link-create/', SocialLinkCreateApiView.as_view()),
    path('social-link-rud/<int:pk>/', SocialLinkRUDApiView.as_view()),
    path('user-social-link-create/', UserSocialLinkCreateApiView.as_view()),
    path('user-social-link-rud/<int:pk>/', UserSocialLinkRUDApiView.as_view()),
]