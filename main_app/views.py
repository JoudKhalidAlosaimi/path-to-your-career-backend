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

            # Convert the DB object we got to JSON using a serializer
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
        
class JobDetail(APIView):

    def get(self,request,job_id):
        try:
            # get a single job using the id fron the DB
            queryset = get_object_or_404(Job, id=job_id)
            # Convert the DB object to JSON
            serializer = JobSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self,request,job_id):
        try:
            # get a single job using the id fron the DB
            queryset = get_object_or_404(Job, id=job_id)

            # Overwrite the single job with the new data using request.data
            serializer = JobSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  # save it if its valid
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self,request,job_id):
        try:
            # Get the single job from the db
            queryset = get_object_or_404(Job, id=job_id)

            # Delete the job
            queryset.delete()

            return Response(
                {"message": f"The job {job_id} has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )