from django.urls import path, re_path
from api import views

urlpatterns = [
    path("v1/apps", views.app_list)
]
