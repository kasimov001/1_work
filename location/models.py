from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name