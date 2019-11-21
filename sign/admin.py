from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','start_time','id']
    search_fields = ['name'] # 搜索栏
    list_filter = ['status'] # 过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] # 搜索栏
    list_filter = ['sign']               # 过滤器
# 2、不加上面这两个类，显示的是一条发布会数据，然而只有发布会名称。

#3、search_fields 用于创建表字段的搜索器，可以设置搜索关键字匹配多个表字段。list_filter 用于创建字段过滤器。

#1、这些代码通知 admin 管理工具为这些模块逐一提供界面
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
