from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.db.models import Sum,Avg,Count,F

# Create your views here.



def queryall_views(request):
    #1.筛选出isActive为True的所有的Author信息
    authors = Author.objects.filter(isActive=True)
    #2.渲染到10-queryall.html模板上
    return render(request,'10-queryall_1.html',locals())

def querybyid_views(request,id):
    author = Author.objects.get(id=id)
    return render(request,'11-querybyid_1.html',locals())

def delete_views(request,id):
    #1.修改id对应的Author的isActive为False
    try:
        au = Author.objects.get(id=id)
        au.isActive = False
        au.save()
    except Exception as e:
        print(e)
    #2.重定向回10-queryall
    return redirect('/10-queryall')

def updateall_views(request):
    Author.objects.all().update(age=F('age')+10) #F查询:专门取对象中某一列值的操作 ,F是用来取值的
    return HttpResponse('更新成功')

def oto_views(request):
    #1.向wife表中增加数据
    #1.1通过外键属性关联数据
    # wife = Wife()
    # wife.wname = "吕夫人Maria"
    # wife.wage = 16
    # wife.author_id = 1 #关联wife与author
    # wife.save()

    #1.2通过关联属性关联数据
    # author = Author.objects.get(id=2)
    # wife = Wife()
    # wife.wname = '魏夫人'
    # wife.wage = 40
    # wife.author = author
    # wife.save()

    #1.3 查询"魏夫人"以及对应的Author的信息
    # wife = Wife.objects.get(wname='魏夫人')
    # print("夫人姓名:%s,夫人年龄:%s,Author姓名:%s,Author年龄:%s"%(wife.wname,wife.wage,wife.author.name,wife.author.age))

    #1.4 查询"吕泽Maria"以及对应的Wife信息
    author = Author.objects.get(name='吕泽Maria')
    print("Author姓名:%s,Wife姓名:%s"%(author.name,author.wife.wname))


    return HttpResponse("查询成功")


def otm_views(request):
    #查询 清华大学出版社所出版的书籍们
    pub = Publisher.objects.get(name="清华大学出版社")
    #获取pub对应的所有的数据信息
    books = pub.book_set.all()

    print("出版社:",pub.name)
    print("书籍：")
    for book in books:
        print("书名:%s,出版时间:%s"%(book.title,book.publicate_date))

    return HttpResponse("查询数据成功")


def otmexer_views(request,pid):
    #pid 表示的是要查看的publisher的id
    # 1.查询所有的publisher
    publishers = Publisher.objects.all()
    #2.查询所有的book
    books = Book.objects.all()
    #根据pid的值来判断查询所有书籍还是按条件查询书籍
    if pid:
        pid = int(pid)
        if pid > 0:
            #按条件筛选book的信息
            #方式1：通过pid直接查询books
            books = Book.objects.filter(publisher_id = pid)

            #方式2：


    return render(request,'16-otm-exer_1.html',locals())












