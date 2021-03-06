# Generated by Django 2.2.5 on 2019-10-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0002_auto_20190930_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='应用名')),
                ('tag', models.CharField(max_length=40, verbose_name='应用标识')),
                ('tier', models.IntegerField(choices=[(0, '前端'), (1, '后端')], verbose_name='架构')),
                ('is_k8s', models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, verbose_name='k8s应用')),
                ('port', models.IntegerField(blank=True, help_text='服务端口', null=True, verbose_name='端口')),
                ('debug', models.IntegerField(choices=[(1, '打开'), (0, '关闭')], default=0, help_text='开放环境: 服务端口+10000, 测试环境: 服务端口+20000, 生产环境: 服务端口+30000', verbose_name='JAVA调试接口')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('env', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='asset.Env', verbose_name='环境')),
                ('hosts', models.ManyToManyField(blank=True, to='asset.Host', verbose_name='主机')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='asset.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '应用管理',
                'verbose_name_plural': '应用管理',
                'ordering': ('id',),
                'unique_together': {('tag', 'env')},
            },
        ),
    ]
