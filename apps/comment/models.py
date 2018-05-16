from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from apps.login.models import User
# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    user = models.ForeignKey(User,max_length=20,on_delete=models.DO_NOTHING,verbose_name='评论用户')
    comment_text = models.TextField(verbose_name='评论')
    comment_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    agree = models.IntegerField(default=0,verbose_name='点赞次数')

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ['-comment_time']
        verbose_name = '评论'
        verbose_name_plural = '评论'