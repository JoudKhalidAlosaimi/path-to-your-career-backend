from rest_framework import serializers
from .models import Job,Course,Bootcamp,Application,UserProfile,Bookmark
from django.contrib.auth import get_user_model
User = get_user_model()

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class BootcampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):

    job_title = serializers.CharField(source='job.title', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    bootcamp_title = serializers.CharField(source='bootcamp.title', read_only=True)

    class Meta:
        model = Application
        fields = '__all__'

class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    # Credits go to https://medium.com/@altafkhan_24475/part-12-a-quick-guide-to-modelserializer-django-rest-framework-7a9753b6efd9
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = UserProfile 
        fields = '__all__'   

    def update(self, instance, validated_data):
        user = instance.user
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.save()

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()

        return instance
