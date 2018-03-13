from numpy import random
from django.shortcuts import render
from django.shortcuts import render_to_response
from apps.blog.models import Blog
from django.db.models import Q
from apps.index.models import Music
from apps.index.spiders.getbiying import Get_biying


def index(request):
    bg = Get_biying()
    music_num = Music.objects.all().count()
    num =random.randint(1,music_num)
    music = Music.objects.get(id=num)
    url_photo = bg.get_one_photo()
    request.session['url_photo'] = url_photo
    request.session['music_id'] = music.music_id
    request.session['music_name'] = music.music_name
    request.session['singer'] = music.singer
    request.session['music_word'] = music.music_word
    return render(request,'index.html',locals())


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            return  render_to_response('index.html')
        else:
            #筛选包含关键字的blog(title or content)
            blogs = Blog.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
            return render_to_response('search_results.html', {'blogs': blogs, 'query': q})
    return render_to_response('search_results.html', {'error': error})


def Carousel(request):
    return render(request,'Carousel.html')