from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect #此处又用到的一个新的类 HttpResponseRedirect，它可以对路径进行重定向，从而将登录成功之后的请求指向/event_manage/目录。
from django.contrib import auth # 认证Django认证模块auth
from django.contrib.auth.decorators import login_required #如果想限制某个视图函数必须登录才能访问，只需要在这个函数的前面加上@login_required 即可
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger # 分页用的
from django.shortcuts import render,get_object_or_404
# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!") # 替换成响应index.html文件了
    '''
    #这里抛弃 HttpResponse 类 ，转而使用 Django 的 render 函数。该函数的第一个参数是请求对象的，第二个参
数返回一个 index.html 页面。
    '''
    return render(request, "index.html")

'''登录动作'''

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) #登录
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!（用户名or密码错误！）'})


'''发布会管理'''
# @login_required
def event_manage(request):
    '''Event.objects.all() 用于查询所有发布会对象（数据），通过 render()函数附加在 event_manage.html 页面返回给客户端浏览器'''
    event_list = Event.objects.all()
    username = request.session.get('user','')  #读取浏览器session
    return render(request,"event_manage.html",{"user":username,"events":event_list})


'''发布会名称搜索'''
# @login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

'''嘉宾管理'''
# @login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)  #把查询出来的所有嘉宾列表 guest_list 放到 Paginator 类中，划分每页显示 2 条数据
    page = request.GET.get('page')  #通过 GET 请求得到当前要显示第几页的数据
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页面不是整数，则提交第一个页面
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页面不在范围内(例如9999)，则提交最后一页的结果整数，提交第一页
        contacts = paginator.page(paginator.num_pages)

    return render(request,"guest_manage.html",{"user":username,"guests":contacts})

'''签到页面'''
@login_required
def sign_index(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,'sign_index.html',{'event':event})

''' 签到动作'''
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    phone = request.POST.get('phone','')
    result = Guest.objects.filter(phone=phone)

    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.'})
    result = Guest.objects.filter(phone=phone,event_id=event_id)

    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event id or phone error.'})
    result = Guest.objects.get(phone=phone,event_id=event_id)

    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':"该用户已签到"})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'签到成功！','guest':result})

'''# 退出登录'''

@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response