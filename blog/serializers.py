from rest_framework import serializers
from .models import (Pages,
                     Blog_category,
                     Blog,
                     Upcoming_events,
                     Course_category,
                     Course,
                     Instructor,
                     Cards)

class Pages_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class Blog_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Blog_serialzer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Upcoming_events_serializer(serializers.ModelSerializer):
    class Meta:
        model = Upcoming_events
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Cource_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Course_category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Cource_serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Instructor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class Cards_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
