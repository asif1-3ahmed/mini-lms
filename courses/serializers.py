# courses/serializers.py
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(read_only=True)  # shows username

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'created_at']
