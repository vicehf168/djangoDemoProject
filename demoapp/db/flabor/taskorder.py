import json
import requests
import time,datetime
import random
import json,requests
from flaborapp.models import *
from eplatformapp.models import *
from corecontractapp.models import *
from humanrunapp.models import UserInfo
from corebillapp.models import *


'''
根据taskname获取task_order数据
'''
def getTaskOrder(taskname):
    # 根据任务名称，获取taskid
    taskId = Task.objects.filter(task_name=taskname).order_by('-id')[:1].values('id')[0]['id']
    # 根据taskid，获取taskorderid
    task_order_id = TaskOrder.objects.filter(task_id=taskId).values('id')[0]['id']
    params = {}
    params['task_order_id'] = task_order_id
    return params