# coding=utf-8
from django.template import Context
from django.template import Template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from table.columns import Link
from table.utils import Accessor


class IconLink(Link):
    """
    Represents a html <a> tag that show image by Bootstrap's icon.
    Example:

    <a href="" class="tooltip-success" data-rel="tooltip" title="编辑">
        <span class="green">
            <i class="icon-edit bigger-120"></i>
        </span>
    </a>
    """

    def __init__(self, operation="edit", *args, **kwargs):
        super(IconLink, self).__init__(*args, **kwargs)

        self.base_attrs['data-rel'] = "tooltip"
        operation_dict = {
            'edit': ["tooltip-success", '编辑', 'green', 'icon-edit'],
            'delete': ["tooltip-error", '删除', 'red', 'icon-trash'],
            'view': ["tooltip-info", '详情', 'blue', 'icon-zoom-in'],
        }
        self.operation_attr = operation_dict.get(operation)
        if not self.operation_attr:
            raise TypeError('the operation (%s) is not defined' % operation)

        self.base_attrs['class'] = self.operation_attr[0]
        self.base_attrs['title'] = self.operation_attr[1]

    @property
    def text(self):
        template = Template("""
            <span class="%s">
                <i class="%s bigger-120"></i>
            </span>
        """ % (self.operation_attr[2], self.operation_attr[3]))
        return template.render(Context())


