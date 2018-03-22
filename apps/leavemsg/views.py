import datetime

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.leavemsg import forms


from .models import *
from apps.blog.models import BlogType
# Create your views here.
BLOG_NUM_EACH_PAGINATOR = 7

def set_page_range(current_page_num,paginator):
    page_range = list(range(max(current_page_num - 2, 1), min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    return page_range

def leave_view(request):
    leave_msg =  LeaveMsg.objects.all()
    blog_types = BlogType.objects.all()


    paginator = Paginator(leave_msg,BLOG_NUM_EACH_PAGINATOR)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num) # 默认page_num为1
    current_page_num = page_of_blogs.number

    page_range = set_page_range(current_page_num,paginator)
    if request.method == 'POST':
        leavemsg_form = forms.LeaveMsgForm(request.POST)
        warning = "留言成功!"

        if leavemsg_form.is_valid():
            msg = leavemsg_form.cleaned_data['msg']

            if msg == None:
                warning = '留言内容不能为空!'
                return render(request,'leave_view.html',locals())

            user = User.objects.get(id=request.session.get('user_id',9999))  #id=9999为默认游客信息
            new_leavemsg =LeaveMsg(user=user,msg=msg,time=datetime.datetime.now())  #插入拥有外键的数据 先获取外键的信息，再一同插入。
            new_leavemsg.save()

    leavemsg_form = forms.LeaveMsgForm()
    return render(request,'leave_view.html',locals())