# Create your views here.
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls import reverse

from apps.comment.models import Comment
from apps.login.models import User

def PostComment(request):

    referer = request.META.get('HTTP_REFERER',reverse('index'))  #之前的url

    user = User.objects.get(id=request.session.get('user_id'))
    comment_text = request.POST.get('text','')

    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))   #整数类型

    model_class = ContentType.objects.get(model=content_type).model_class() #得到该数据模型(Blog)
    model_obj = model_class.objects.get(id=object_id)

    #text为空??

    comment = Comment()
    comment.user = user
    comment.comment_text = comment_text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)