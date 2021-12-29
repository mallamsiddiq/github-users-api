from django.contrib import admin
from django.urls import include, path
from blog import views

#from newsite import blog


handler404 = views.error_404


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]