from django.urls import path
from .views import JobsIndex,JobDetail

urlpatterns = [
    path('jobs/', JobsIndex.as_view(), name='job_index'),
    path('jobs/<int:job_id>/', JobDetail.as_view(), name='job_detail')
]