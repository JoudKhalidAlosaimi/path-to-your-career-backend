from django.contrib import admin
from .models import Job,Course,Bootcamp,Application,UserProfile

# Register your models here.
admin.site.register(Job)
admin.site.register(Course)
admin.site.register(Bootcamp)
admin.site.register(Application)
admin.site.register(UserProfile)
