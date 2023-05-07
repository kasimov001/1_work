from rest_framework import serializers
from ..models import News


class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'image', 'description', 'create_date', 'views_count']
