from django.db import models

class Music(models.Model):
    music_name = models.CharField(max_length=50,verbose_name='歌名')
    music_word = models.CharField(max_length=100,verbose_name='歌词')
    music_id = models.IntegerField(verbose_name='歌曲id',default=0) #网易云的歌曲id
    singer = models.CharField(max_length=50,verbose_name='歌手')

    def __str__(self):
        return self.music_name

    class Meta:
        verbose_name = '歌曲'
        verbose_name_plural = '歌曲'