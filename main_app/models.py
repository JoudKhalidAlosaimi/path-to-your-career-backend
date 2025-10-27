from django.db import models

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
