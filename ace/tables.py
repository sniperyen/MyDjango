# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from table import Table
from table.columns import Column, LinkColumn, Link, CheckboxColumn
from table.columns.base import ColumnHeader

from ace.models import Node
from table.utils import A

# 参考: https://github.com/shymonk/django-datatable
from ace.table_ext import IconLink


class NodeTable(Table):
    check = CheckboxColumn(header='')
    id = Column(field='id', header='ID')
    node_name = Column(field='node_name', header='名称')
    node_type = Column(field='node_type', header='类型')
    node_address = Column(field='node_address', header='地址')
    node_contact = Column(field='node_contact', header='联系人')
    node_remarks = Column(field='node_remarks', header='备注')
    node_signtime = Column(field='node_signtime', header='创建时间')
    action = LinkColumn(header='操作',
                        links=[
                            IconLink(operation='view', viewname='view', args=('node', A('id'))),
                            IconLink(operation='edit', viewname='edit', args=('node', A('id'))),
                            IconLink(operation='delete', viewname='delete', args=('node', A('id')))]
                        )

    class Meta:
        model = Node
        info = True
        search = True
        # search_placeholder = '搜索'
        # info_format = '总共 _TOTAL_'
        # zero_records = '没有数据'
        # pagination = True
        # pagination_first = '首页'
        # pagination_last = '末页'
        # pagination_prev = '上一页'
        # pagination_next = '下一页'

        # ajax = True
        # ajax_source = reverse_lazy('node_list')
