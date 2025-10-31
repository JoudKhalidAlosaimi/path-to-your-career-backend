from rest_framework import serializers
from .models import Job,Course,Bootcamp,Application,UserProfile
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
    class Meta:
        model = Application
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = UserProfile
        fields = "__all__"