前段时间遇到需要在数据库中初始化约2k个model实例用于实现类似邀请码的功能，发现使用Django提供的signal很是好用，
对于这种应用，使用post_syncdb很容易实现。当然还有其他的方法可用，这里主要通过这个实例来讲Django的signal实现。

## Signal简介
django 包含一个称为 signal dispatcher, 使得框架内其他松耦合或不相关的应用在某些特定的事件发生后得到通知， 
即在特定事件发生时, 使用signal 能够通知指定的接收者。这在多个代码片段同时关注同一特定事件时显得尤为有用。Django内置Signal主要有：

```
Signals
  Model signals
      pre_init
      post_init
      pre_save
      post_save
      pre_delete
      post_delete
      m2m_changed
      class_prepared
  Management signals
      post_syncdb
  Request/response signals
      request_started
      request_finished
      got_request_exception
  Test signals
      setting_changed
      template_rendered
  Database Wrappers
      connection_created
```
      
## post_syncdb signal
post_syncdb是在应用安装后 syncdb命令或者flush命令触发的，django-admin.py flush 命令
用于将数据库还原为初次运行 syncdb命令后的状态。

## Signal的监听
要接收应用的signal，需要利用 Signal.connect() 方法来定义接收函数（receiver function ），以数据库的初始化为例：

model.py
```
from django.db import models

class Passwd(models.Model):
    passwd=models.CharField(max_length=10, help_text='Maximum 10 characters.')
    status = models.BooleanField(default=True)
    usedtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.passwd

    class Meta:
        verbose_name_plural = "Passwords"
```

management.py

```
from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
from django.dispatch import receiver
from invite_code import models as invite_app
from invite_code.models import Passwd


'''生成八位数字和字母组成的随机序列用于邀请码'''
from random import choice
import string
def GenPasswd(length=8, chars= string.letters+string.digits):
    while True:
        yield ''.join([choice(chars) for i in range(length)])

def pass_gen(sender, **kwargs):
    line1=list()
    for i in xrange(2000):
        for item in GenPasswd():
            line1.append(item)
    line2=list(set(line1))
    for str in line2:
        p=Passwd(passwd=str, status=1)
        p.save()

post_syncdb.connect(pass_gen, sender= invite_app)
也可以使用装饰器的receiver方法：

from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
from django.dispatch import receiver
from invite_code import models as invite_app
from invite_code.models import Passwd

@receiver(pre_save, sender=invite_app)
def pass_gen(sender, **kwargs):
    '''同上'''

```
需要注意的是，和其他signal不同的是，
**post_syncdb 必须和model（例子中invite_app，即整个table ）绑定而不是models中的Passwd（table中的列）绑定。**