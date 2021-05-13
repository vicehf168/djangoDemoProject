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
根据taskName获取work表数据
'''
def getFlaborSettlementWork(taskName):
    # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    # 根据taskid查询workid
    workId = FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values('work_id')[0]['work_id']
    params = {}
    params['workId'] = workId
    return params