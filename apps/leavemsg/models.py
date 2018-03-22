from django.db import models
from apps.blog.models import User
# Create your models here.
class LeaveMsg(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='留言用户')
    msg = models.CharField(max_length=200,verbose_name='留言信息')
    time = models.DateTimeField(auto_now_add=True,verbose_name='留言时间')

    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ['-time']
        verbose_name = '留言'
        verbose_name_plural = '留言'