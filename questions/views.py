from django.shortcuts import render
import time
import datetime
from django.http import HttpResponse
from .models import *
# from models import BookInfo,HeroInfo
# Create your views here.

def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request,'index.html')
def index(request):
    list = BookInfo.objects.all()

    return render(request, 'index.html',{'list': list})

def my_render(request, template_name, comtext_dict={}):

    # 1.加载模板文件  去模板目录下面获取html文件的内容，得到一个模板对象。
    temp = loader.get_template(template_name)
    # 2.定义模板上下文  向模板文件传递数据。
    comtext = RequestContext(request, comtext_dict)
    # 3.模板渲染  得到一个标准的html内容
    res_html = temp.render(comtext)
    # 返回页面内容
    return HttpResponse(res_html)

# 图书的展示页面
def show_books(request):
    
    list = BookInfo.objects.all()
    # 传递参数
    
    # return render(request, 'show_books.html',{'list': list})
    return render(request, 'index.html',{'list': list})


# 英雄的展示页面 关联查询
def detail(request, bid):

    book = BookInfo.objects.get(id=bid)

    heros = book.heroinfo_set.all()

    return render(request, 'booktest/detail.html',
                  {'heros': heros, 'book': book})


