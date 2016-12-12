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

        self.attrs['data-rel'] = "tooltip"
        operation_dict = {
            'edit': ["tooltip-success", '编辑', 'green', 'icon-edit'],
            'delete': ["tooltip-error", '删除', 'red', 'icon-trash'],
            'view': ["tooltip-info", '详情', 'blue', 'icon-zoom-in'],
        }
        if operation not in operation_dict:
            raise TypeError('the operation (%s) is not exists' % operation)

        operation_attr = operation_dict.get(operation)
        self.attrs['class'] = operation_attr[0]
        self.attrs['title'] = operation_attr[1]
        self.span = """
            <span class="%s">
                <i class="%s bigger-120"></i>
            </span>
        """ % (operation_attr[2], operation_attr[3])


    def render(self, obj):
        """ Render link as HTML output tag <a>.
        """
        self.obj = obj
        attrs = ' '.join([
             '%s="%s"' % (attr_name, attr.resolve(obj))
             if isinstance(attr, Accessor)
             else '%s="%s"' % (attr_name, attr)
             for attr_name, attr in self.attrs.items()
             ])
        return '<a %s>%s</a>' % (attrs, self.span)