from django.urls import path, re_path, include
from api import views

urlpatterns = [
    path("v1/apps", views.AppList.as_view()),
    path("v1/hosts", views.HostList.as_view()),
    path("v1/envs", views.EnvList.as_view()),
    path("v1/projects", views.ProjectList.as_view()),
    re_path("v1/apps/(?P<pk>.*)/", views.AppDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
