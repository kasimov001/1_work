from django.contrib import admin
from .models import Contact, SocialLink, UserSocialLink

admin.site.register(Contact)
admin.site.register(SocialLink)
admin.site.register(UserSocialLink)

