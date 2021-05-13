from django.shortcuts import render,HttpResponse,redirect
import time,datetime
from flaborapp.models import *
from demoapp.common.frontinit import *
from demoapp.db.dboperate import *
from demoapp.service.serviceoperate import *
from demoapp.createdata.forwardPublicTask import *
from demoapp.createdata.forwardInviteTask import *
from demoapp.createdata.createSettlementOrder import *
from django.http import JsonResponse
import json


# Create your views here.


def homepage(request):
    # return HttpResponse('hello django')
    # print(request.GET)
    t = time.ctime()
    '''
    render响应返回demo.html文件，前提是django框架需要先找到这个文件，再返回给请求方
    django初始会先加载settings文件，render读取的html文件的路径要配置在settings文件中
    settings文件中，在TEMPLATES中的属性DIRS配置读取html文件的路径
    '''
    # return render(request, 'homepage.html')

    '''
    {'time':t}表示，将t赋值给time创给前端html，前端在通过{{time}}的方式获取值
    也可以通过locals()方式，直接将变量传给前端html，前端直接通过{{t}}的方式获取值
    '''

    # if request.GET.get('user') == 'hufei':
    #     return redirect('/demoapp/login')
    # return render(request, 'homepage.html', {'time':t})
    #locals()表示所有本地变量的集合，在本函数中无论定义多少个变量，只要传了locals()，就不需要传具体的变量了，html中直接取本函数中定义的变量
    # return render(request,'homepage.html',locals())
    pass

def test(request):
    # l = ['胡飞','谢锋','少宇']
    # d = {'name':'谢锋','sex':'男','height':'180'}
    # cap = 'fher'
    # cat = 'hdj jjh k'
    # tt = datetime.datetime.now()
    # deft = ''
    # return render(request,'login.html',locals())
    '''
    下面表示获取task表中id=1012的记录，获取的是一个QuerySet对象
    '''
    # taskName = Task.objects.filter(id=1012)
    #不同的获取方式，与下面的效果一样
    # print(type(taskName.values_list('task_name')[0][0]))
    # print(taskName.values_list('task_name')[0][0])
    '''
    taskName.values('task_name')，表示将上面的QuerySet对象（即表中的记录），筛选出字段task_name
    筛选出来的还是一个QuerySet对象，再通过taskName.values('task_name')[0]，获取第一条记录，是一个dict
    dict就可以通过key-value的形式获取到值了
    '''
    # print(type(taskName.values('task_name')[0]['task_name']))
    # print(taskName.values('task_name')[0]['task_name'])
    # return HttpResponse(str(taskName.values('task_name')[0]['task_name']))

    '''
    正向-非全-支付宝-公开抢单
    '''
    # print('用户名###################',request.POST.get('username'))
    # ForwardPublishTask().testPublishTask(FrontInit().b_login_token())
    # ForwardPublishTask().commondata()
    return HttpResponse('Success!')


# -------------------------------------------------以下正文----------------------------------------------


'''
正向公开抢单任务
'''
def forwardPublicTask(request):
    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    # 三目运算：a if b else c ，if b成立取a，否则取b
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择发布的任务类型
    public_TaskType = str.strip(request.GET.get('publicTaskType'))
    # 业务处理
    if taskno:
        ServiceOperate().forwardPublicTaskService(b_token, public_TaskType, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            # 若不足5位数，前面补0拼凑成5位数
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().forwardPublicTaskService(b_token, public_TaskType, username, tasknumber)
    return HttpResponse('Success!')


'''
正向邀请任务
'''
def forwardInviteTask(request):
    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的被邀请人手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择发布的任务类型
    invite_TaskType = str.strip(request.GET.get('inviteTaskType'))
    # 业务处理
    if taskno:
        ServiceOperate().forwardInviteTaskService(b_token, invite_TaskType, username, taskno, mobile)
    elif tasknumber:
        timeNow = str(time.time())[-5:]    # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().forwardInviteTaskService(b_token, invite_TaskType, username, tasknumber, mobile)
    return HttpResponse('Success!')


'''
初始化所有B端用户名
'''
def queryUserName(request):
    userNames = ServiceOperate().queryUserNameService()
    return JsonResponse(userNames,safe=False)


'''
生成B端待结算订单
'''
def createSettlementOrder(request):

    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    settlementType = str.strip(request.GET.get('settlementType'))

    # 业务处理
    if taskno:
        ServiceOperate().createSettlementOrderService(b_token, settlementType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createSettlementOrderService(b_token, settlementType, mobile, username, tasknumber)
    return HttpResponse('Success!')


'''
生成B端待验收订单
'''
def createAcceptanceOrder(request):
    print('来了老哥验收')
    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    acceptanceType = str.strip(request.GET.get('acceptanceType'))
    # 业务处理
    if taskno:
        ServiceOperate().createAcceptanceOrderService(b_token, acceptanceType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createAcceptanceOrderService(b_token, acceptanceType, mobile, username, tasknumber)
    return HttpResponse('Success!')


'''
生成大V端待审核订单
'''
def createReviewOrder(request):

    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    reviewType = str.strip(request.GET.get('reviewType'))
    # 业务处理
    if taskno:
        ServiceOperate().createReviewOrderService(b_token, reviewType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createReviewOrderService(b_token, reviewType, mobile, username, tasknumber)
    return HttpResponse('Success!')


'''
生成大V端待支付订单
'''
def createPayOrder(request):

    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    payType = str.strip(request.GET.get('payType'))
    # 业务处理
    if taskno:
        ServiceOperate().createPayOrderService(b_token, payType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createPayOrderService(b_token, payType, mobile, username, tasknumber)
    return HttpResponse('Success!')


'''
生成小V端待审核订单
'''
def createXvReviewOrder(request):

    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    xvReviewType = str.strip(request.GET.get('xvReviewType'))
    # print(payType,mobile,username,tasknumber)
    # 业务处理
    if taskno:
        ServiceOperate().createXvReviewOrderService(b_token, xvReviewType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createXvReviewOrderService(b_token, xvReviewType, mobile, username, tasknumber)
    return HttpResponse('Success!')


'''
生成小V端待费用发放订单
'''
def createXvFeeIssueOrder(request):

    # 获取输入的用户名
    username = str.strip(request.GET.get('username'))
    # 获取输入的密码
    password = str.strip(request.GET.get('pwd'))
    # 获取输入的任务编号
    taskno = str.strip(request.GET.get('taskno')) if request.GET.get('taskno') else ''  # strip直接对None会报错
    # 获取输入的任务数量
    tasknumber = str.strip(request.GET.get('tasknumber')) if request.GET.get('tasknumber') else ''
    # 获取输入的手机号
    mobile = str.strip(request.GET.get('mobile'))
    # 调B登录接口获取token
    b_token = FrontInit().b_login_token(username, password)
    # 获取选择的任务类型
    xvFeeIssuType = str.strip(request.GET.get('xvFeeIssueType'))
    # print(payType,mobile,username,tasknumber)
    # 业务处理
    if taskno:
        ServiceOperate().createXvFeeIssueOrderService(b_token, xvFeeIssuType, mobile, username, taskno)
    elif tasknumber:
        timeNow = str(time.time())[-5:]  # 时间戳后5位
        for f in range(1,int(tasknumber)+1):
            tasknumber = str(f).zfill(5)
            tasknumber = str(timeNow) + tasknumber
            ServiceOperate().createXvFeeIssueOrderService(b_token, xvFeeIssuType, mobile, username, tasknumber)
    return HttpResponse('Success!')