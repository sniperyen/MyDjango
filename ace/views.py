# coding=utf-8
import logging
import datetime
import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from ace.forms import LineForm
from ace.forms import NodeForm, DeviceForm
from ace.models import Node, Line, Device
from ace.tables import NodeTable
from utils.util_web import TemplateViewBase, ListViewBase


__author__ = 'sanyang'


class HomePageView(TemplateViewBase):
    template_name = 'ace/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['sub_title'] = '控制台'
        return context


class DomainView(TemplateViewBase):
    template_name = 'ace/domain_list.html'

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        return context


class CommonListView(ListViewBase):
    pass


from table.views import FeedDataView


class NodeListView(FeedDataView):
    token = NodeTable.token

    def get_queryset(self):
        return super(NodeListView, self).get_queryset().filter(id__gt=5)


# 显示各列表信息
def lists(request, table):
    if table == 'node':
        data = Node.objects.all()
        data = NodeTable(data)
        list_template = 'ace/node_list.html'
        sub_title = '节点管理'
    if table == 'line':
        data = Line.objects.all()
        list_template = 'ace/line_list.html'
        sub_title = '线路信息'
    if table == 'device':
        data = Device.objects.all()
        list_template = 'ace/device_list.html'
        sub_title = '设备信息'
        # 建立context字典，将值传递到相应页面
    context = {
        'object_list': data,
        'table': table,
        'sub_title': sub_title,
    }
    # 跳转到相应页面，并将值传递过去
    return render(request, list_template, context)


def add(request, table):
    # 根据提交的请求不同，获取来自不同Form的表单数据
    if table == 'node':
        form = NodeForm(request.POST or None)
        sub_title = '添加节点'
    if table == 'line':
        form = LineForm(request.POST or None)
        sub_title = '添加线路'
    if table == 'device':
        form = DeviceForm(request.POST or None)
        sub_title = '添加设备'
        # 判断form是否有效
    if form.is_valid():
        # 创建实例，需要做些数据处理，暂不做保存
        instance = form.save(commit=False)
        # 将登录用户作为登记人
        if table == 'node':
            instance.node_signer = request.user
        if table == 'line':
            instance.line_signer = request.user
        if table == 'device':
            instance.device_signer = request.user
            # 保存该实例
        instance.save()
        # 跳转至列表页面,配合table参数，进行URL的反向解析
        return redirect('lists', table=table)

        # 创建context来集中处理需要传递到页面的数据
    context = {
        'form': form,
        'table': table,
        'sub_title': sub_title,
    }
    # 如果没有有效提交，则仍留在原来页面
    return render(request, 'base_add.html', context)


def edit(request, table, pk):
    if table == 'line':
        # 这是Django的一个快捷方法,通过pk去line表中取值，如果有值则返回，如果无值则抛出http404的异常
        # 具体信息可参考https://docs.djangoproject.com/en/1.9/topics/http/shortcuts/
        table_ins = get_object_or_404(Line, pk=pk)
        # 通过instance来将Form的数据做填充
        form = LineForm(request.POST or None, instance=table_ins)
        sub_title = '修改线路信息'
    if table == 'node':
        table_ins = get_object_or_404(Node, pk=pk)
        form = NodeForm(request.POST or None, instance=table_ins)
        sub_title = '修改机构信息'
    if table == 'device':
        table_ins = get_object_or_404(Device, pk=pk)
        form = DeviceForm(request.POST or None, instance=table_ins)
        sub_title = '修改设备信息'
        # 判断form是否有效
    if form.is_valid():
        # 创建实例，需要做些数据处理，暂不做保存
        instance = form.save(commit=False)
        # 将登录用户作为登记人,在修改时，一定要使用str强制,因为数据库中以charfield方式存放了登记人
        if table == 'node':
            instance.node_signer = str(request.user)
        if table == 'line':
            instance.line_signer = str(request.user)
        if table == 'device':
            instance.device_signer = str(request.user)
            # 保存该实例
        instance.save()
        # 跳转至列表页面,配合table参数，进行URL的反向解析
        return redirect('lists', table=table)

    context = {
        'table': table,
        'form': form,
        'sub_title': sub_title,
    }
    # 与res_add.html用同一个页面，只是edit会在res_add页面做数据填充
    return render(request, 'base_add.html', context)


def delete(request, table, pk):
    return HttpResponse('xx')