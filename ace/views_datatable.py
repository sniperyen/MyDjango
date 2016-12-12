# coding=utf-8
from django.db.models import Q
from django.shortcuts import render_to_response
from Lib.django_datatables_view.base_datatable_view import BaseDatatableView

from ace.models import Node

# 参考： http://django-datatable-view.readthedocs.io/en/latest/topics/index.html


class ProxyListJson(BaseDatatableView):
    model = Node  # 要分页的类

    columns = ['id', 'node_name', 'node_type', 'node_address', 'node_contact', 'node_remarks', 'node_signtime', 'id']  # 需要显示的字段
    order_columns = ['', 'node_name', 'node_type', 'node_address', 'node_contact', 'node_remarks', 'node_signtime', '']  # 排序
    max_display_length = 500

    def render_column(self, row, column):
        return super(ProxyListJson, self).render_column(row, column)