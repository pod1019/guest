"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from django.urls import include
from sign import views #导入sign应用views文件


urlpatterns = [

    # path(r'admin/', admin.site.urls),
    # path(r'index/',views.index), #添加index/路径配置
    # path(r'login_action/',views.login_action), #配置登录处理
    # path(r'event_manage/',views.event_manage),
    # path(r'accounts/login/',views.index),
    # path(r'search_name/',views.search_name),
    # path(r'guest_manage/',views.guest_manage),
    # path(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),  # 配置签到
    # path(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),  # 添加签到路径的路由

    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index), #添加index/路径配置
    url(r'^login_action/', views.login_action), #配置登录处理
    url(r'^event_manage/', views.event_manage),
    url(r'^accounts/login/', views.index),
    url(r'^search_name/', views.search_name),
    url(r'^guest_manage/', views.guest_manage),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index), #配置签到
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action), # 添加签到路径的路由
    url(r'^logout/$', views.logout), #添加退出目录的路由
    url(r'^api/', include('sign.urls', namespace="sign")),



]
