from django.db import models

# Create your models here.
class CommentPost(models.Model):
    User = models.CharField(max_length=20,verbose_name='评论用户')
    Comment = models.CharField(max_length=100,verbose_name='评论')
    CommentTime = models.DateField(verbose_name='评论时间')
    Agree = models.IntegerField(verbose_name='点赞次数')

    def __str__(self):
        return self.Comment

    class Meta:
        ordering = ['-CommentTime']
        verbose_name = '评论'
        verbose_name_plural = '评论'