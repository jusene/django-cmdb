# Generated by Django 2.2.7 on 2020-01-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_project_arch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='lan',
            field=models.GenericIPAddressField(verbose_name='内网地址'),
        ),
    ]
