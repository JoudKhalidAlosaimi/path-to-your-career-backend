from django.urls import path
from .views import JobsIndex,JobDetail,CoursesIndex,CourseDetail,BootcampsIndex,BootcampDetail,ApplicationIndex,ApplicationDetail,RegisterUser,UserProfileDetail,BookmarkIndex,BookmarkDetail,UserProfileDelete
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('jobs/', JobsIndex.as_view(), name='job_index'),
    path('jobs/<int:job_id>/', JobDetail.as_view(), name='job_detail'),
    path('courses/', CoursesIndex.as_view(), name='course_index'),
    path('courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),
    path('bootcamps/', BootcampsIndex.as_view(), name='bootcamp_index'),
    path('bootcamps/<int:bootcamp_id>/', BootcampDetail.as_view(), name='bootcamp_detail'),
    path('applications/', ApplicationIndex.as_view(), name='application_index'),
    path('applications/<int:application_id>/', ApplicationDetail.as_view(), name='application_detail'),
    path('bookmarks/', BookmarkIndex.as_view(), name='bookmark_index'),
    path('bookmarks/<int:bookmark_id>/', BookmarkDetail.as_view(), name='bookmark_detail'),
    path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='user_register'),
    path('profile/', UserProfileDetail.as_view(), name='user_profile'),
    path('profile/delete/<int:user_id>/', UserProfileDelete.as_view(), name='user_delete')
]