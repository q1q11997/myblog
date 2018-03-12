from django.db import models

class Music(models.Model):
    music_name = models.CharField(max_length=50,verbose_name='歌名')
    music_word = models.CharField(max_length=100,verbose_name='歌词')
    music_url = models.URLField(max_length=200,verbose_name='歌曲地址')
    singer = models.CharField(max_length=50,verbose_name='歌手')

    def __str__(self):
        return self.music_name

    class Meta:
        verbose_name = '歌曲'
        verbose_name_plural = '歌曲'