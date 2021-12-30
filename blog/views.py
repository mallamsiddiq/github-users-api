from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import render
import json
from .serializers import PostSerializer
from .models import github_users
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.views.decorators.cache import cache_page




def error_404(request, exception):
    data = {}
    return render(request,'blog/error.html', data)

@cache_page(60 * 10)
def home(request):
  data = github_users.objects.all()
  pagination = request.GET.get('pagination')
  page=request.GET.get('page')
  paginator = Paginator(data, 25)
  if pagination:
    paginator = Paginator(data, pagination)
  data = paginator.get_page(1)
  if page:
        try:
          data = paginator.get_page(page)
        except ValueError:
          return HttpResponse("<h1>Input valid parameters</h1>")
  return render(request, 'blog/base.html', {'git_user':data})

def index(request,page=1):
  data = github_users.objects.all()
  pagination = request.GET.get('pagination')
  paginator = Paginator(data, 25)
  if pagination:
    paginator = Paginator(data, pagination)
  data = paginator.get_page(page)
  return render(request, 'blog/base.html', {'git_user':data})

def user_detail(request, user_pk=6):
  try:
    data = github_users.objects.all().get(id=user_pk)
    return render(request, 'blog/base_home.html', {'git_user':data})
  except ObjectDoesNotExist:
    return HttpResponse("<h1>You're searching a user that's not registered with Us yet.</h1>")


def swagger_param(token,desc,obj_type):
  return (openapi.Parameter(token, in_=openapi.IN_QUERY, description=desc, type=f'openapi.TYPE_{obj_type}'))



class PostView(APIView):
    username_param=swagger_param('username','get a specific user by username','STRING')
    user_pk_param = swagger_param('id','get a specific user by username','INTEGER')
    page_param = swagger_param('page','Get a specific page number noting the default pagination is 25 ','INTEGER')
    order_by_param = swagger_param('order_by','Get an ordered response in your parameters of choice noting the default pagination is 25 ','INTEGER')
    pagination_param = swagger_param('pagination','paginate the response of list of users','INTEGER')
    serializer_class = PostSerializer
    @swagger_auto_schema(manual_parameters=[username_param,page_param,user_pk_param,order_by_param,pagination_param])
    def get(self, request, format=None):
      user_pk = request.GET.get('id')
      username = request.GET.get('username')
      order_by = request.GET.get('order_by')
      pagination = request.GET.get('pagination')
      page = request.GET.get('page')
      data = github_users.objects.all()
      if username:
        data = github_users.objects.filter(name=username.lower())
        if not data:
          return HttpResponse("<h1>You're searching a user that's not registered with Us yet.</h1>")
      elif user_pk:
        try:
          data = github_users.objects.filter(id=user_pk)
        except ValueError:
          return HttpResponse("<h1>Input valid parameters</h1>")
        if not data:
          return HttpResponse("<h1>You're searching a user that's not registered with Us yet.</h1>")
      elif order_by:
        try:
          data = github_users.objects.order_by(order_by)
        except Exception as e:
          return HttpResponse(e)
      paginator = Paginator(data, 25) 
      if pagination:
        paginator = Paginator(data, pagination)
      data = paginator.get_page(1)
      if page:
        try:
          data = paginator.get_page(page)
        except ValueError:
          return HttpResponse("<h1>Input valid parameters</h1>")
      data = PostSerializer(data,many=True).data
      #return Response(data, status=status.HTTP_200_OK)
      return JsonResponse(data, safe=False)