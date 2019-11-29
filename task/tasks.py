from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import task
import requests
from utils.AnsibleUtil import AnsibleRun

@task
def ansible_hoc(host_list, task_list):
    adhoc = AnsibleRun(host_list, task_list)
    adhoc.task_run()
    return adhoc.get_result()

@task
def clean_image(env):
    dev_k8s = 'http://192.168.66.155:8080/api/v1/nodes'
    prod_k8s = 'http://192.168.66.128:8080/api/v1/nodes'
    choice = {
       'dev': dev_k8s,
       'prod': prod_k8s
    }
    hosts = []
    resp = requests.get(choice.get(env))
    for node in  resp.json().get('items'):
        t = node.get('metadata').get('name')
        hosts.append(t)
    host_list = ','.join(hosts)
    task_list = [{"action": {"module": "shell", "args": "docker rmi `docker images -qa`"}},]
    adhoc = AnsibleRun(host_list, task_list)
    adhoc.task_run()
    return adhoc.get_result()

    
