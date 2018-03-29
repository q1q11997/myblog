from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from apps.blog.models import Blog,BlogType
from apps.comment.models import Comment
from apps.login.models import User

BLOG_NUM_EACH_PAGINATOR  = 7  #设置每页的blog数量

#显示当前页数的前后各两页并且控制范围，超出范围的用'...'号表示。
def set_page_range(current_page_num,paginator):
    page_range = list(range(max(current_page_num - 2, 1), min(current_page_num + 2, paginator.num_pages) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    return page_range

#显示全部博客视图(分页) 返回 blog_list,blog_count
def blog_list(request):
    blog_list = Blog.objects.all()
    blog_count = blog_list.count()
    blog_types = BlogType.objects.all()
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')  # 取所有发布过Blog的月份 返回Y:m

    #类型分类博客数量统计
    blog_types_list = []

    for type in blog_types:
        type.blog_count_by_type = Blog.objects.filter(blog_type =type).count()
        blog_types_list.append(blog_type)

    #日期分类博客数量统计
    blog_dates_dict = {}

    for blog_date in blog_dates:
        blog_count_by_date = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count_by_date


    paginator = Paginator(blog_list,BLOG_NUM_EACH_PAGINATOR)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num) # 默认page_num为1
    current_page_num = page_of_blogs.number

    page_range = set_page_range(current_page_num,paginator)

    return render(request,'blog_list.html', locals())

#显示单个博客视图，取创建时间最接近的前后博客，阅读数+1操作 返回 blog,previous_blog,next_blog
def blog_each(request,blog_id):
    blog = get_object_or_404(Blog,id=blog_id)
    blog_types = BlogType.objects.all()
    previous_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()


    #右边的面板/最热博客需要的数据

    hot_blogs = Blog.objects.all().order_by('-read_num')


    # 右边的面板/最新博客需要的数据
    new_blogs =Blog.objects.all().order_by('-created_time')



    if not request.COOKIES.get('blog_%s_read' % blog.id):  #cookie中没有访问记录
        blog.read_num +=1
        blog.save()

    user = User.objects.get(id=request.session.get('user_id',9999)) # id=9999为游客

    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.id).order_by('-comment_time')

    response = render(request,'blog_each.html',locals())
    response.set_cookie('blog_%s_read' % blog.id ,'true')
    return response

#显示单个类型的全部博客视图 返回blog_type blog_list_by_type(符合类型的Blog列表)
def blog_type(request,blog_type_id):
    blog_type = get_object_or_404(BlogType,id=blog_type_id)
    blog_types = BlogType.objects.all()
    blog_list_by_type = Blog.objects.filter(blog_type_id = blog_type_id)
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')  # 取所有发布过Blog的月份 返回Y:m

    #类型分类博客数量统计
    blog_types_list = []

    for type in blog_types:
        type.blog_count_by_type = Blog.objects.filter(blog_type =type).count()
        blog_types_list.append(blog_type)

    #日期分类博客数量统计
    blog_dates_dict = {}

    for blog_date in blog_dates:
        blog_count_by_date = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count_by_date

    paginator = Paginator(blog_list_by_type, BLOG_NUM_EACH_PAGINATOR)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)  # 默认page_num为1
    current_page_num = page_of_blogs.number

    page_range = set_page_range(current_page_num, paginator)

    return render(request,'blog_type_list.html',locals())

#显示该月份发布的全部博客
def blog_by_date(request,year,month):

    blog_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    blog_date = '%s年%s月' %(year,month)
    blog_count = blog_list.count()
    blog_types = BlogType.objects.all()
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')  # 取所有发布过Blog的月份 返回Y:m

    #类型分类博客数量统计
    blog_types_list = []

    for type in blog_types:
        type.blog_count_by_type = Blog.objects.filter(blog_type =type).count()
        blog_types_list.append(blog_type)

    #日期分类博客数量统计
    blog_dates_dict = {}

    for blog_date in blog_dates:
        blog_count_by_date = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count_by_date

    paginator = Paginator(blog_list, BLOG_NUM_EACH_PAGINATOR)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)  # 默认page_num为1
    current_page_num = page_of_blogs.number

    page_range = set_page_range(current_page_num, paginator)
    return render(request,'blog_date_list.html',locals())