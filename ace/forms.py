# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from .models import Node, Line, Device


# 定义Node的Form,Form名字为 模式名+Form
class NodeForm(ModelForm):
    class Meta:
        model = Node
        exclude = ['node_signer']  # 在Form中不显示node_signer这个字段


class LineForm(ModelForm):
    class Meta:
        model = Line
        exclude = ['line_signer']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = ['device_signer']