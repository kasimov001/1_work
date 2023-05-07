from django.contrib import admin
from .models import User, userRole, role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'middle_name', 'username', 'email', 'location', 'number', 'birthdate']
    search_fields = ['firstname', 'lastname', 'username', 'birthdate']


admin.site.register(userRole)
admin.site.register(role)
