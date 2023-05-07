from rest_framework import serializers
from ..models import role, userRole, User


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ['id', 'name', 'descriptions']


class UserRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = userRole
        fields = ['id', 'user', 'role']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'middle_name', 'username', 'email', 'location', 'number', 'birthdate']
