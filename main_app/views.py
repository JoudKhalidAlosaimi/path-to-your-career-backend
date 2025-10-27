from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Job
from .serializers import JobSerializer

# Create your views here.

class JobsIndex(APIView):
    
    def get(self, request):
        try:
            # get all of the jobs from the DB
            queryset = Job.objects.all()

            # Convert the DB object we got to JSON
            serializer = JobSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            # take the data from the request and put it in a serializer
            serializer = JobSerializer(data=request.data)

            # if the data is valid, save it
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

