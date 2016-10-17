# coding=utf-8
import logging
import datetime
import uuid

from django.http import HttpResponse
from tasks import *
from djcelery.models import PeriodicTask, IntervalSchedule, CrontabSchedule

__author__ = 'sanyang'


def add_task(request, seconds):
    if request.method == 'GET':
        logging.info(seconds)
        if seconds:  # 几秒后执行任务
            # 重复任务
            int_sche = IntervalSchedule.objects.filter(every=seconds, period='seconds')
            if int_sche:
                int_sche = int_sche[0]
            else:
                int_sche = IntervalSchedule()
                int_sche.every = seconds
                int_sche.period = 'seconds'
                int_sche.save()

            # 定时任务(也可以是重复的，不能精确到秒)
            # cron_sche = CrontabSchedule()
            # cron_sche.minute = 1
            # cron_sche.hour = 1
            # cron_sche.day_of_week = '0,1,2'
            # cron_sche.day_of_month = '0,1,2'
            # cron_sche.month_of_year = '0,1,2'
            # cron_sche.save()

            pt =  PeriodicTask()
            pt.name = u'每隔 %sS 执行一次任务 %s' % (seconds, str(uuid.uuid1()))  # name 是唯一的，故后缀了uuid
            pt.task = 'demo_celery.tasks.add'
            pt.interval= int_sche  # interval 和 schedule 这两个属性只能选一个
            # pt.crontab = cron_sche
            # pt.expires = datetime.datetime.now() + datetime.timedelta(days=1)
            pt.save()


        else:
            res = add.delay(2, 3)
            return HttpResponse(HttpResponse(res.result))


from django.contrib import messages

def testmail(request):
    try:
        messages.success(request, '服务器运行正常!.')
    except Exception, e:
        messages.error(request, '由于下列原因,这个URL不能被监听.<br>'+ str(e) )