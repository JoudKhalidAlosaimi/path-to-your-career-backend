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

    job_title = serializers.CharField(source='job.title', read_only=True)
    job_description = serializers.CharField(source='job.description',read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description',read_only=True)
    bootcamp_title = serializers.CharField(source='bootcamp.title', read_only=True)
    course_description = serializers.CharField(source='course.description',read_only=True)

    class Meta:
        model = Bookmark
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    # https://medium.com/%40titoadeoye/django-backend-foundations-extending-with-django-rest-framework-b28aad6eef53
    # https://youtu.be/Q9iYzhaUZEI?si=XZjdShTj9OQhNdy0
    first_name = serializers.CharField(source='user.first_name',required=False)
    last_name = serializers.CharField(source='user.last_name',required=False)
    email = serializers.EmailField(source='user.email',required=False)

    class Meta:
        model = UserProfile 
        fields = '__all__'   

    def update(self, instance, validated_data):
            user_data = validated_data.pop('user', {}) 
            user = instance.user

            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            return instance
