from django.db import models
from access.models import User
from location.models import District


class Category(models.Model):
    title = models.CharField(max_length=221)
    description = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Worker(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min_salary = models.CharField(max_length=99, blank=True, null=True)
    max_salary = models.CharField(max_length=99, blank=True, null=True)
    deadlink = models.DateTimeField(max_length=99, auto_now_add=True)
    demand = models.TextField(max_length=221)
    more_info = models.TextField(max_length=221)
    workingtime = models.CharField(max_length=99)
    call_time = models.CharField(max_length=99)
    status = models.TextField()

    def __str__(self):
        return self.author


class job(models.Model):
    ROLE = (
        (0, "Male"),
        (1, "woman"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    min_salary = models.CharField(max_length=99, blank=True, null=True)
    max_salary = models.CharField(max_length=99, blank=True, null=True)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    deadlink = models.DateTimeField(max_length=99, auto_now_add=True)
    demand = models.TextField(max_length=221)
    benefit = models.CharField(max_length=221)
    location = models.IntegerField()
    more_info = models.TextField(max_length=221)
    gender = models.IntegerField(choices=ROLE, default=0)
    workingtime = models.CharField(max_length=221)
    call_time = models.CharField(max_length=221)
    status = models.TextField(max_length=221)

    def __str__(self):
        return self.title

