from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Job,Course,Bootcamp,Application,UserProfile
from .serializers import JobSerializer,CourseSerializer,BootcampSerializer,ApplicationSerializer,UserProfileSerializer,UserSerializer


# Create your views here.

User = get_user_model()

class JobsIndex(APIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]
    def get(self,request,job_id):
        try:
            # TODO :
            # get a single job from the DB using the id=job_id
            # Convert the DB object to JSON using a serializer
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
            # get a single job from the DB using the id=job_id
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
            # get a single job from the DB using the id=job_id
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
    permission_classes = [AllowAny]
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
        
class CourseDetail(APIView):
    permission_classes = [AllowAny]
    def get(self,request,course_id):
        try:
            # TODO :
            # get a single course from the DB
            # Convert the course to JSON
            # return a response with a status
            queryset = get_object_or_404(Course, id=course_id)

            serializer = CourseSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self,request,course_id):
        try:
            # TODO :
            # get a single course from the DB
            # Overwrite the single course
            # save it if its valid
            # return a response and status
            queryset = get_object_or_404(Course, id=course_id)

            serializer = CourseSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self,request,course_id):
        try:
            # TODO :
            # Get the single course from the DB 
            # Delete the course
            # return a response and a status
            queryset = get_object_or_404(Course, id=course_id)

            queryset.delete()

            return Response(
                {"message": f"The course {course_id} has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class BootcampsIndex(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        try:
            # TODO :
            # get all the bootcamp objects from the DB
            # convert them to JSON
            # return a response with the status
            queryset = Bootcamp.objects.all()

            serializer = BootcampSerializer(queryset, many=True)

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
            serializer = BootcampSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class BootcampDetail(APIView):
    permission_classes = [AllowAny]
    def get(self,request,bootcamp_id):
        try:
            # TODO :
            # get a single bootcamp from the DB
            # Convert the single bootcamp to JSON
            # return a response with a status
            queryset = get_object_or_404(Bootcamp, id=bootcamp_id)

            serializer = BootcampSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self,request,bootcamp_id):
        try:
            # TODO :
            # get a single bootcamp from the DB
            # Overwrite the single bootcamp
            # save it if its valid or return a 400 BAD REQUEST
            # return a response and status
            queryset = get_object_or_404(Bootcamp, id=bootcamp_id)

            serializer = BootcampSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self,request,bootcamp_id):
        try:
            # TODO :
            # Get the single bootcamp from the DB
            # Delete the bootcamp
            # return a response and a status
            queryset = get_object_or_404(Bootcamp, id=bootcamp_id)

            queryset.delete()

            return Response(
                {"message": f"The bootcamp {bootcamp_id} has been successfully deleted."},
                status=status.HTTP_204_NO_CONTENT
            )

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class ApplicationIndex(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        try:
            # TODO :
            # get all the applications from the DB
            # convert them to JSON
            queryset = Application.objects.filter(owner=request.user)

            serializer = ApplicationSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            # TODO :
            # take the data from the request and put it in a serializer
            # if the data is valid, save it and return a 201 CREATED 
            # if it's not valid return 400 BAD REQUEST
            serializer = ApplicationSerializer(data=request.data)

            if serializer.is_valid():
                job = request.data.get('job')
                course = request.data.get('course')
                bootcamp = request.data.get('bootcamp')

                application_exits = Application.objects.filter(
                    owner=request.user,
                    job=job,
                    course=course,
                    bootcamp=bootcamp,
                ).exists()

                if application_exits:
                    return Response(
                        {"error": "You have already applied for this."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ApplicationDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,application_id):
        try:
            # TODO :
            # get a single application using the id from the DB
            # Convert the single application to JSON using serializer

            queryset = get_object_or_404(Application, id=application_id)

            serializer = ApplicationSerializer(queryset)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self,request,application_id):
        try:
            # TODO :
            # get a single application
            # Overwrite the application
            # save it
            queryset = get_object_or_404(Application, id=application_id)

            serializer = ApplicationSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self,request,application_id):
        try:
            # TODO :
            # get the single application from the DB
            # Delete it

            queryset = get_object_or_404(Application,id=application_id)

            queryset.delete()

            return Response(
                    {"message": f"The application {application_id} has been successfully deleted."},
                    status=status.HTTP_204_NO_CONTENT
                )

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Please enter a username and password'}, 
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'The username already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'The email already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password
        )

        UserProfile.objects.create(user=user)

        return Response(
            {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
        },
            status=status.HTTP_201_CREATED)
    
class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            serializer = UserProfileSerializer(request.user.profile)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def put(self,request):
        try:
            serializer = UserProfileSerializer(request.user.profile, data=request.data, partial = True)

            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response(
                {"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )