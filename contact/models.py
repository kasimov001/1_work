from django.db import models
from access.models import User


class Contact(models.Model):
    there = models.CharField(max_length=221)
    more_info = models.TextField()
    number = models.CharField(max_length=221, blank=True, null=True)

    def __str__(self):
        return self.number


class SocialLink(models.Model):
    name = models.CharField(max_length=221, blank=True, null=True)
    url = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class UserSocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SocialLink = models.ForeignKey(SocialLink, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


