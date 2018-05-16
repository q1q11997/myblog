import json
from datetime import datetime, date

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from apps.login.models import User
from apps.blog.models import Blog
from apps.leavemsg.models import LeaveMsg
from apps.comment.models import Comment
# Create your views here.

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def space_json(request,user_id):
    if not request.session.get('is_login',None):
        return redirect('index')

    user = get_object_or_404(User, id=user_id)

    blogs = Blog.objects.filter(author_id=user_id)

    comments = Comment.objects.filter(user_id=user_id)

    comment_dict = {}
    obj_list =[]
    obj_id_list = []
    comment_type = []
    comment_obj_ids = []

    for comment in comments:
        obj_type = comment.content_type
        obj_list.append(obj_type)

    obj_types = set(obj_list)  #获得评论的所有种类

    for obj_type in obj_types:
        comment_objs = comments.filter(content_type=obj_type) #取得所有该类型的评论
        comment_dict[obj_type.name] = None #初始化字典

        list_of_objs = {}

        for comment_obj in comment_objs:
            name = obj_type.name #取得评论的obj类型
            obj = {
                "msg":{
                    "obj_type": name,                             #obj类型 (如博客,留言*待开发*等)
                    "obj_type_id":comment_obj.content_type.id,    #obj类型id
                    "obj_id": comment_obj.id,                     #obj的id
                    "obj_text": comment_obj.comment_text,         #评论的内容
                    "obj_time":comment_obj.comment_time,          #评论时间
                    }
            }

            # 以comment_dict['obj_type']['comment_obj.id']查找当前obj

            list_of_objs[comment_obj.id] = obj
            comment_dict[name] = list_of_objs


    json_comment = json.dumps(comment_dict,cls=CJsonEncoder) #序列化datetime

    return HttpResponse(json_comment,content_type="application/json",charset='utf-8')


import json
from django.http import HttpResponse, response


def space(request,user_id):
    user = get_object_or_404(User,id=user_id)
    blogs = Blog.objects.filter(author=user)
    return render(request,'space.html',locals())