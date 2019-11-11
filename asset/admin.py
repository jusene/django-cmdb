from django.contrib import admin
from asset.models import Project, Env, Idc, Server, Host, User, Computer

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'site', 'comment')
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(Env)
class EnvAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(Idc)
class IdcAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'model', 'virtual', 'colored_status', 'admin', 'comment')
    search_fields = ('name', 'ip')
    list_filter = ('status', 'model')
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lan', 'wan', 'server', 'idc', 'env',
                    'project', 'cpu', 'memory', 'use', 'colored_status', 'admin', 'comment')
    search_fields = ('name', 'lan', 'wan')
    list_filter = ('server', 'idc', 'env', 'project', 'status')
    list_per_page = 50
    list_display_links = ('id', 'name')



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'email', 'phone', 'comment')
    list_per_page = 50
    list_display_links = ('id', 'name')


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset_id', 'unit', 'os', 'model', 'num', 'location', 'lock', 'domain', 'user', 'comment')
    search_fields = ['asset_id', 'user__name']
    list_per_page = 50
    list_display_links = ('id', 'asset_id')
