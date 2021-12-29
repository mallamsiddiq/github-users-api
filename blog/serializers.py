from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import github_users



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = github_users
        fields = ('id','name',"Type","date_created","avatar_url",'url','html_url')