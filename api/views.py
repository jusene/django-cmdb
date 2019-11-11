from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from django.http import Http404
from api.serializers import AppSerializer, HostSerializer, EnvSerializer, ProjectSerializer
from app.models import App
from asset.models import Env, Host, Project


# Create your views here.
class AuthPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class AppList(APIView):
    permission_classes = [AuthPermission, ]
    '''
    List all apps
    '''
    def get(self, request, format=None):
        apps = App.objects.all()
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppDetail(APIView):
    '''
    AppList a app detail
    '''
    def get_object(self, pk, env):
        try:
            return App.objects.get(tag=pk, env=env)
        except Exception as e:
            raise Http404

    def get(self, request, pk, format=None):
        env = request.GET.get('env')
        if env is None:
            app = App.objects.filter(tag=pk)
            serializer = AppSerializer(app, many=True)
            return Response(serializer.data)
        else:
            env_id = Env.objects.get(tag=env).id
            app = self.get_object(pk=pk, env=env_id)
            serializer = AppSerializer(app)
            return Response(serializer.data)


class HostList(APIView):
    def get(self, request, format=None):
        hosts = Host.objects.all()
        serializer = HostSerializer(hosts, many=True)
        return Response(serializer.data)


class EnvList(APIView):
    def get(self, request, format=None):
        envs = Env.objects.all()
        serializer = EnvSerializer(envs, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


