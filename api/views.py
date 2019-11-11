from rest_framework import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app.models import App
from asset.models import Env, Host


# Create your views here.
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"


@csrf_exempt
def app_list(request):
    if request.method == "GET":
        if request.GET.get('app') and request.GET.get('env'):
            env_id = Env.objects.get(tag=request.GET.get('env'))
            serializer = AppSerializer(App.objects.get(tag=request.GET.get('app'), env=env_id))
            row = dict(serializer.data)
            if row.get("is_k8s") == 0 and Host.objects.get(id=row.get('hosts')[0]).idc_id == 1:
                row["hosts"] = list(map(lambda x: Host.objects.get(id=x).wan, row.get('hosts')))
            else:
                row["hosts"] = list(map(lambda x: Host.objects.get(id=x).lan, row.get('hosts')))
            return JsonResponse(row)
        else:
            apps = App.objects.all()
            serializer = AppSerializer(apps, many=True)
            return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"Message": "Method is not allowed!"})
