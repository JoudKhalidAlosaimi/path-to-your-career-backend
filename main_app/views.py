from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Job,Course
from .serializers import JobSerializer,CourseSerializer

# Create your views here.

class JobsIndex(APIView):
    
    def get(self, request):
        try:
            # TODO :
            # get all the jobs objects from the DB
            # convert them to JSON
            # return the converted JSON.data and a status
            queryset = Job.objects.all()

            serializer = JobSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            # TODO :
            # take the data from the request and put it in a serializer
            # if the data is valid, save it
            serializer = JobSerializer(data=request.data)

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
            # TODO :
            # get a single job using the id fron the DB
            # Convert the DB object to JSON
            queryset = get_object_or_404(Job, id=job_id)

            serializer = JobSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self,request,job_id):
        try:
            # TODO :
            # get a single job using the id fron the DB
            # Overwrite the single job with the new data using request.data
            # save it if its valid
            queryset = get_object_or_404(Job, id=job_id)

            serializer = JobSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self,request,job_id):
        try:
            # TODO :
            # Get the single job from the db using the id
            # Delete the job
            queryset = get_object_or_404(Job, id=job_id)

            queryset.delete()

            return Response(
                {"message": f"The job {job_id} has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class CoursesIndex(APIView):
    def get(self,request):
        try:
            # TODO :
            # get all the course objects from the DB
            # convert them to JSON
            # return the converted JSON.data and a status
            queryset = Course.objects.all()

            serializer = CourseSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
                return Response(
                    {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
    def post(self,request):
        try:
            # TODO :
            # take the data from the request and put it in a serializer
            # if the data is valid, save it
            # return a response with a status
            serializer = CourseSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )