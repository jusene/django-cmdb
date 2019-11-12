from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import task
from utils.AnsibleUtil import AnsibleRun

@task
def ansible_hoc(host_list, module, args):
    adhoc = AnsibleRun(host_list, module, args)
    adhoc.task_run()
    return adhoc.get_result()
