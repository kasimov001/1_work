from rest_framework import serializers
from ..models import job, Worker, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description']


class JobGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = job
        fields = ['id', 'author', 'category', 'district', 'title', 'min_salary', 'max_salary', 'min_age', 'max_age',
                  'deadlink', 'demand', 'benefit', 'location', 'more_info', 'gender', 'workingtime', 'call_time',
                  'status']


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = ['id', 'author', 'category', 'district', 'title', 'min_salary', 'max_salary', 'min_age', 'max_age',
                  'deadlink', 'demand', 'benefit', 'location', 'more_info', 'gender', 'workingtime', 'call_time',
                  'status']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class WorkerGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Worker
        fields = ['id', 'author', 'category', 'min_salary', 'max_salary', 'deadlink', 'demand', 'more_info',
                  'workingtime', 'call_time', 'status']


class WorkerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'author', 'category', 'min_salary', 'max_salary', 'deadlink', 'demand', 'more_info',
                  'workingtime', 'call_time', 'status']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance
