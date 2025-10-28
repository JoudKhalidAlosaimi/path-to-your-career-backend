from django.urls import path
from .views import JobsIndex,JobDetail,CoursesIndex,CourseDetail,BootcampsIndex,BootcampDetail,ApplicationIndex,ApplicationDetail

urlpatterns = [
    path('jobs/', JobsIndex.as_view(), name='job_index'),
    path('jobs/<int:job_id>/', JobDetail.as_view(), name='job_detail'),
    path('courses/', CoursesIndex.as_view(), name='course_index'),
    path('courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),
    path('bootcamps/', BootcampsIndex.as_view(), name='bootcamp_index'),
    path('bootcamps/<int:bootcamp_id>/', BootcampDetail.as_view(), name='bootcamp_detail'),
    path('applications/', ApplicationIndex.as_view(), name='application_index'),
    path('applications/<int:application_id>/', ApplicationDetail.as_view(), name='application_detail')
]