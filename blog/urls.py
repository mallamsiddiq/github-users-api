from django.urls import path, include, re_path


from . import views
from .views import PostView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Github Users' API ",
      default_version='v1',
      description="""<p><b>This is the customised view of the Github users' API, you can view and query with parameters on the bar shown below </b><p> 
                        <p><i>Click the Get icon, scroll down to twick with the parameters, query with 'username', 'id'; 
                        order by any of the parameters and you can also change the pagination and specify the page you noting however that the default 
                        pagination is '25'.</i><br><br><br><br><span> Play around with the raw json response at the base url above</span><p><br><br>""",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mallamsiddiq@gmail.com"),
      license=openapi.License(name="UMBA License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

   path('costum-api/', schema_view.with_ui('swagger', cache_timeout=0), name='costum-api'),

   path('users/', views.home, name='home'),
   path('users/<int:page>/', views.index, name='index'),
   path('api/users/profiles/', PostView.as_view(),name='all_users_api'),
   path('users/details/<int:user_pk>/', views.user_detail, name='user_detail'),
]

handler404 = views.error_404

#re_path('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),