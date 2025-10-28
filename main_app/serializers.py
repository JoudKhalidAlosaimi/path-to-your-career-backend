from rest_framework import serializers
from .models import Job,Course,Bootcamp,Application,UserProfile

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

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"