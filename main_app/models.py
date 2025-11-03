from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

STATUS = (
    ('Open', 'Open'),
    ('Closed', 'Closed')
)
class Job(models.Model):
    title = models.CharField()
    company = models.CharField()
    description = models.CharField()
    status = models.CharField(choices=STATUS,default=STATUS[0][0])
    link = models.URLField(blank=True)


    def __str__(self):
        return f'{self.title} - {self.status}'
    

class Course(models.Model):
    title = models.CharField()
    provider = models.CharField()
    description = models.CharField()
    duration = models.DurationField()
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title} - {self.provider}'
    
class Bootcamp(models.Model):
    title = models.CharField()
    provider = models.CharField()
    description = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.title} - {self.provider}'


APPLICATION_STATUS = (
    ('Applied', 'Applied'),
    ('Interview', 'Interview'),
    ('Rejected', 'Rejected')
)
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(choices=APPLICATION_STATUS, default=APPLICATION_STATUS[0][0],null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.job != None:
            return f'{self.job.title} - {self.status}'
        elif self.course != None:
            return f'{self.course.title} - {self.status}'
        elif self.bootcamp != None:
            return f'{self.bootcamp.title} - {self.status}'
        else:
            return 'No applications made yet'

class Bookmark(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE,null=True,blank=True)
    is_bookmarked = models.BooleanField(default=True)

    def __str__(self):
        if self.job != None:
            return f'{self.job.title} - {self.is_bookmarked}'
        elif self.course != None:
            return f'{self.course.title} - {self.is_bookmarked}'
        elif self.bootcamp != None:
            return f'{self.bootcamp.title} - {self.is_bookmarked}'
        else:
            return 'No bookmarks made yet'

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    gender = models.CharField(choices=GENDER,null=True,blank=True)
    # https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial
    profile_image = models.ImageField(upload_to='profile_images/',null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


