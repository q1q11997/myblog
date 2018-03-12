from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=20,verbose_name='类型名称')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客类型'
        verbose_name_plural = '博客类型'


class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    read_num =models.IntegerField(default=0,verbose_name='阅读人数')
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,verbose_name='博客类型')
    title = models.CharField(max_length=20,verbose_name='标题')
    content = RichTextUploadingField(verbose_name='内容')                                                    #富文本类型
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    last_updated_time = models.DateTimeField(auto_now=True,verbose_name='最后更新时间')


    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created_time']
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'


