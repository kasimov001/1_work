from django.db import models


class News(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    views_count = models.CharField(max_length=221)

    def __str__(self):
        return self.title