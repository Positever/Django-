from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    #1.定义在列表页上要显示的字段们
    #属性：list_display
    #取值：有属性名称组成的元组或列表
    list_display = ('name','email','age')

    #2.定义在列表页上能够链接到详情页的字段们
    #属性：list_display_links
    #取值：由属性名臣组成的元组或列表
#     注意：取值必须出现在list_display中
    list_display_links = ('email',)

    #3.定义在列表页中就允许被编辑的字段们
    #属性：list_editable
    #取值：由属性名称组成的元组或列表
    #注意：取值必须出现在list_display中但不能出现在list_display_links中
    list_editable = ('name',)

    #4.定义在列表页的右侧增加过滤器实现快速筛选
    #属性：list_filter
    #取值：由属性名称组成的元组或列表
    list_filter = ('isActive',)

    #5.添加搜索字段
    #属性：search_fields
    #取值：由属性名称
    search_fields = ('name','age')

    #7.在详情页中，指定要显示的字段以及显示的顺序
    #属性：fields
    #取值：由属性名组成的元组或列表，元组或列表中的是顺序决定了在详情页中的显示顺序
    # fields = ('age','name','email')

    #8.在详情页中，对字段进行分组
    #属性：fieldsets
    #注意：fields和fieldsets是不能共存的
    fieldsets = (
        #分组1-包含name和age两个列
        ('基本选项',{
            "fields":('name','age'),
        }),
        #分组2-包含email和isActive两个列
        ('高级选项',{
            "fields":('email','isActive'),
            "classes":("collapse",)
        })
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ("title","publicate_date")
    #6.指定日期分层选择器
    #属性：date_hierarchy
    #取值：必须为DateField或DateTimeField
    date_hierarchy = "publicate_date"

class WifeAdmin(admin.ModelAdmin):
    list_display = ('wname','wage')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','country')
    list_display_links = ('address',)
    list_editable = ('name',)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife,WifeAdmin)