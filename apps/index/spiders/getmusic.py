import json
from urllib import parse
import urllib.request as ur
from apps.index import models
from numpy import random


class Get_music(object):


    def get_one_music(self,music_name):
        name = parse.quote(music_name)
        url=r'http://s.music.163.com/search/get/?type=1&s='+name+'&limit=10'
        headers={
            'User-Agent': 'Mozilla / 4.0(compatible;MSIE6.0;Windows NT 5.1)'
        }

        request=ur.Request(url,headers=headers)
        response=ur.urlopen(request)
        html_byte=response.read()
        html_string=html_byte.decode('utf-8')
        #解析成字典形式,图片保存在images的key中:
        dict_json=json.loads(html_string)
        #得到images的key所包含的图片信息:

#       得到list_photo中的第三张图片组成的字典
        dict={
                'music_name':dict_json['result']['songs'][0]['name'],
                'music_word': '暂缺',
                'music_id':dict_json['result']['songs'][0]['id'],
                'singer':dict_json['result']['songs'][0]['artists'][0]['name'],

        }

#       lyric_url = r'http://music.163.com/api/lyric?os=pc&id='+dict['music_id']+'&lv=-1&kv=-1&tv=-1'
        new_music = models.Music.objects.create()
        new_music.music_name = dict['music_name']
        new_music.music_word = dict['music_word']
        new_music.music_id = dict['music_id']
        new_music.singer = dict['singer']
        new_music.save()

        #dict=list_photo[num]
        #得到图片的残缺url
        #url_photo=dict['url']
        #将图片的残缺url组合成一个完整的url
        #url_photo=r'http://cn.bing.com'+url_photo
        return dict


