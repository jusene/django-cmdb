from django.db import models
from asset.models import Host, Env, Project
from django.utils.html import format_html


# Create your models here.
class App(models.Model):
    name = models.CharField('应用名', max_length=30)
    tag = models.CharField('应用标识', max_length=40)
    tier = models.IntegerField('架构', choices=((0, "前端"), (1, "后端")))
    env = models.ForeignKey(Env, on_delete=models.CASCADE, verbose_name="环境", default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目", default=None)
    is_k8s = models.IntegerField('k8s应用', choices=((0, "否"), (1, "是")), default=1)
    hosts = models.ManyToManyField(Host, verbose_name='主机', blank=True)
    port = models.IntegerField('端口', null=True, blank=True, help_text='服务端口')
    lang = models.IntegerField("语言", choices=((0, "java"), (1, 'js'), (2, 'nodejs'), (3, "python")), default=0)
    debug = models.IntegerField('JAVA调试接口', choices=((1, "打开"), (0, "关闭")), default=0,
                                help_text="开放环境: 服务端口+10000, "
                                "测试环境: 服务端口+20000, "
                                "生产环境: 服务端口+30000")
    url = models.URLField("URL", null=True, blank=True)
    surl = models.URLField("URL", null=True, blank=True)
    comment = models.TextField("备注", null=True, blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.tag

    def site(self):
        if self.surl:
            return format_html('<a href={} target="_blank">{}</a><br/><a href={} target="_blank">{}</a>', self.url, self.url, self.surl, self.surl)
        else:
            return format_html('<a href={} target="_blank">{}</a>', self.url, self.url)

    site.short_description = "URL"

    class Meta:
        verbose_name = "应用管理"
        verbose_name_plural = "应用管理"
        ordering = ("id", )
        unique_together = ("tag", "env")

class DB(models.Model):
    name = models.CharField('数据库', max_length=30)
    ip = models.GenericIPAddressField('IP地址', unique=True)
    port = models.IntegerField('端口')
    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=30)
    comment = models.TextField("备注", null=True, blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "数据库管理"
        verbose_name_plural = "数据库管理"
        ordering = ("id", )


class Middle(models.Model):
    name = models.CharField('中间件', max_length=30)
    entry = models.CharField('入口', max_length=50)
    username = models.CharField('用户名', max_length=20, null=True, blank=True)
    password = models.CharField('密码', max_length=30, null=True, blank=True)
    comment = models.TextField("备注", null=True, blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "中间件管理"
        verbose_name_plural = "中间件管理"
        ordering = ("id", )

