from django.contrib import admin
from app.models import App, DB, Middle
from django.http import HttpResponse
import csv

# Register your models here.
def export_csv(modeladmin, request, queryset):
    tier_choice = {0: "前端", 1: "后端"}
    is_k8s_choice = {0: "否", 1: "是"}
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposion'] = 'attachment:filename="apps.csv"'
    writer = csv.writer(response)
    writer.writerow(['序号', '应用名', '应用标识', '架构', '环境', '项目', '端口', 'k8s应用', '部署主机', 'URL', '备注'])
    for index, row in enumerate(queryset.all(), 1): 
        #print(index, row.name, row.tag, tier_choice.get(row.tier), row.env, row.project, row.port, is_k8s_choice.get(row.is_k8s), list(map(lambda x: x.lan if not x.wan else x.lan+'|'+x.wan,row.hosts.all())), row.url+";"+(row.surl if row.surl else ''), row.comment)
        writer.writerow([index, row.name, row.tag, tier_choice.get(row.tier), row.env, row.project, row.port, is_k8s_choice.get(row.is_k8s), list(map(lambda x: x.lan if not x.wan else x.lan+' | '+x.wan,row.hosts.all())), row.url+" | "+(row.surl if row.surl else ''), row.comment])
    return response
export_csv.short_description = "导出"

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tag', 'tier', 'env', 'project', 'port', 'is_k8s', 'debug', 'site', 'comment')
    list_per_page = 50
    list_editable = ('debug',)
    search_fields = ("tag",)
    list_filter = ("tier", "env", "project")
    filter_horizontal = ('hosts', )
    actions = (export_csv,)


@admin.register(DB)
class DBAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'port', 'comment')
    list_per_page = 50
    

@admin.register(Middle)
class Middle(admin.ModelAdmin):
    list_display = ('id', 'name', 'entry', 'comment')
    list_per_page = 50
