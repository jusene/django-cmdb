# Generated by Django 2.2.5 on 2019-10-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='surl',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
