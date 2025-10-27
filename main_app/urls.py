from django.urls import path
from .views import JobsIndex,JobDetail,CoursesIndex

urlpatterns = [
    path('jobs/', JobsIndex.as_view(), name='job_index'),
    path('jobs/<int:job_id>/', JobDetail.as_view(), name='job_detail'),
    path('courses/', CoursesIndex.as_view(), name='course_index')
]