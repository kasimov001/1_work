from django.contrib import admin
from .models import Category, Worker, job


admin.site.register(Category)
admin.site.register(Worker)
admin.site.register(job)

