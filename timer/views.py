# coding:utf-8
from django.http import HttpResponse
from django.utils.translation import ugettext as _
import time


def index(request):
    # if request.REQUEST == 'GET':
    return HttpResponse(_(u'Hello world!'))


def test1_view(request):
    t = time.localtime()
    n = t[6]  # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
    weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'),
                _('Friday'), _('Saturday'), _('Sunday')]
    return HttpResponse(weekdays[n])