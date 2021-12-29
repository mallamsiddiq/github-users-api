from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class github_users(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    avatar_url= models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    html_url= models.CharField(max_length=100,default='')
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
    	ordering = ['-id']

    
    def __str__(self):
        return self.name +" " + str(self.date_registered)