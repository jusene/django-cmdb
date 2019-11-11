from django.db import models
from django.utils.html import format_html
from asset.utils.useful_data import status_code, unit_code


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='项目名称', max_length=30, unique=True)
    tag = models.CharField(verbose_name='项目标识', max_length=10, unique=True)
    comment = models.TextField(verbose_name='备注', null=True, blank=True)
    arch = models.URLField("URL", null=True, blank=True, help_text='生产环境应用架构拓扑图')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name
    
    def site(self):
        return format_html('<a href={}>{}</a>', self.arch, self.name+"应用拓扑")   
    site.short_description = '应用拓扑' 
 
    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = "项目管理"
        ordering = ['id']


class Env(models.Model):
    name = models.CharField(verbose_name='环境名称', max_length=20, unique=True)
    tag = models.CharField(verbose_name='环境标识', max_length=10, unique=True)
    comment = models.TextField(verbose_name='备注', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "环境管理"
        verbose_name_plural = "环境管理"
        ordering = ['id']


class Idc(models.Model):
    name = models.CharField("机房名称", max_length=20, unique=True)
    tag = models.CharField("机房标识", max_length=20, unique=True)
    comment = models.TextField("备注", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机房管理"
        verbose_name_plural = "机房管理"
        ordering = ['id']


class User(models.Model):
    name = models.CharField("用户名", max_length=20)
    email = models.EmailField("邮箱")
    phone = models.CharField("手机", max_length=11)
    number = models.CharField("工号", max_length=20)
    comment = models.TextField("备注", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = "用户管理"
        ordering = ['id']


class Server(models.Model):
    name = models.CharField("主机名", max_length=20, unique=True)
    ip = models.GenericIPAddressField('IP地址', unique=True)
    cpu = models.CharField('CPU(C)', max_length=10)
    memory = models.CharField('内存(G)', max_length=10)
    model = models.CharField('型号', max_length=100, default=None)
    virtual = models.CharField('虚拟化技术', max_length=20, default='KVM')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="管理员", default=None)
    status = models.IntegerField('状态', choices=status_code, default=0)
    comment = models.TextField('备注', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

    def colored_status(self):
        if self.status == 0:
            colord_code = "006400"
        elif self.status == 1:
            colord_code = 'FFD700'
        else:
            colord_code = 'FF0000'
        return format_html(
            '<span style="color:#{};">{}</span>',
            colord_code, dict(status_code).get(self.status)
        )
    colored_status.short_description = "状态"

    class Meta:
        verbose_name = "物理机管理"
        verbose_name_plural = "物理机管理"
        ordering = ['id']


class Host(models.Model):
    name = models.CharField("主机名", max_length=20, unique=True)
    lan = models.GenericIPAddressField("内网地址", unique=True)
    wan = models.GenericIPAddressField("外网地址", null=True, blank=True, help_text="可选")
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name="物理机", null=True, blank=True, default=None)
    idc = models.ForeignKey(Idc, on_delete=models.CASCADE, verbose_name="机房", default=None)
    env = models.ForeignKey(Env, on_delete=models.CASCADE, verbose_name='环境', default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="项目", null=True, blank=True, default=None)
    use = models.CharField("用途", max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="管理员", default=None)
    cpu = models.CharField('CPU(C)', max_length=10)
    memory = models.CharField('内存(G)', max_length=10)
    status = models.IntegerField('状态', choices=status_code, default=0)
    comment = models.TextField('备注', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s" % (self.name, self.lan, self.wan if self.wan else "")

    def colored_status(self):
        if self.status == 0:
            colord_code = "006400"
        elif self.status == 1:
            colord_code = 'FFD700'
        else:
            colord_code = 'FF0000'
        return format_html(
            '<span style="color:#{};">{}</span>',
            colord_code, dict(status_code).get(self.status)
        )
    colored_status.short_description = "状态"

    class Meta:
        verbose_name = "虚拟机管理"
        verbose_name_plural = "虚拟机管理"
        ordering = ['id']


class Computer(models.Model):
    asset_id = models.CharField("资产编号", max_length=20)
    unit = models.IntegerField('部件', choices=unit_code, default=0)
    os = models.CharField('操作系统', max_length=20, blank=True, null=True)
    model = models.CharField('型号', max_length=50)
    num = models.IntegerField('数量')
    location = models.CharField('位置', max_length=20)
    lock = models.IntegerField('机箱锁', choices=((0, "否"), (1, "是")), blank=True, null=True)
    domain = models.IntegerField('脱域', choices=((0, "否"), (1, "是")), blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name="使用人")
    comment = models.TextField('备注', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asset_id

    class Meta:
        verbose_name = "PC管理"
        verbose_name_plural = "PC管理"
        ordering = ['id']
