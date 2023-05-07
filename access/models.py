from django.db import models


class role(models.Model):
    name = models.TextField(max_length=222)
    descriptions = models.TextField()

    def __str__(self):
        return self.name


class userRole(models.Model):
    user = models.TextField(max_length=222, blank=True, null=True)
    role = models.ForeignKey(role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user


class User(models.Model):
    firstname = models.CharField(max_length=221, blank=True, null=True)
    lastname = models.CharField(max_length=221, blank=True, null=True)
    middle_name = models.CharField(max_length=221)
    username = models.CharField(max_length=221, blank=True, null=True)
    email = models.EmailField(null=True)
    location = models.IntegerField()
    number = models.CharField(max_length=221, blank=True, null=True)
    birthdate = models.DateField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.firstname


