# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Node, Line, Device


# 对NodeAdmin进行个性化配置
class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_name', 'node_address', 'node_signer') # 在list页面上显示指定的字段
    exclude = ['node_signer'] # 在编辑、新增页面上排除node_signer的选项

    # 对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.node_signer = str(request.user)
        obj.save()


class LineAdmin(admin.ModelAdmin):
    exclude = ('line_signer',)

    def save_model(self, request, obj, form, change):
        obj.line_signer = str(request.user)
        obj.save()


class DeviceAdmin(admin.ModelAdmin):
    exclude = ('device_signer',)

    def save_model(self, request, obj, form, change):
        obj.device_signer = str(request.user)
        obj.save()


admin.site.register(Node, NodeAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Device, DeviceAdmin)