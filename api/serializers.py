from rest_framework import serializers
from app.models import App
from asset.models import Host, Env, Project


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = "__all__"


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

