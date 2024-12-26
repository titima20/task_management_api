from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 
                 'status', 'completed', 'completed_at', 'created_at', 'updated_at', 'user_id']
        read_only_fields = ['created_at', 'updated_at', 'completed_at']

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future")
        return value

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status']

    def validate(self, data):
        instance = getattr(self, 'instance', None)
        if instance and instance.completed and 'status' not in data:
            raise serializers.ValidationError("Completed tasks cannot be edited unless status is changed")
        return data
