from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import task
from utils.AnsibleUtil import AnsibleRun

@task
def ansible_hoc(host_list, task_list):
    adhoc = AnsibleRun(host_list, task_list)
    adhoc.task_run()
    return adhoc.get_result()
