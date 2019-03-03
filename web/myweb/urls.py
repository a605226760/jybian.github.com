from django.conf.urls import url,include
from .import views
import myweb
# from imgTest.views import uploadImg # 添加

urlpatterns = [
    # 主页
    url(r'^$',views.index,name='index'),

    # 关于我们
    url(r'^about$',views.about,name='about'),

    # 联系我们
    url(r'^contact$',views.contact,name='contact'),

    # 产品展示默认项
    url(r'^product_list$',views.product_list,name='product_list'),

    # 产品展示
    url(r'^product_list/(?P<name>\w+)$',views.product_lists,name='product_lists'),

    # 产品下二级页面
    url(r'^yumi/(?P<name>\w+)$',views.yumi,name='yumi'),

    # 详情页面
    url(r'^product_info/(?P<uid>\w+)/(?P<name>\w+)$',views.product_info,name='product_info'),

    # 报错信息页面
    url(r'^error$',views.error,name='error'),
    #新闻
    url(r'^new_info$',views.new_info,name='new_info'),

    #app端页面

    # 集团简介
    url(r'^introduce$', views.introduce, name='intro'),

    # 核心技术
    url(r'^news$', views.jishu, name='jishu'),

    #产品（一级）
    url(r'^product$',views.product, name='product'),

    #水稻（二级）
    url(r'^product_(?P<name>\w+)$',views.shuidao, name='shuidao'),

    #三级文件夹
    url(r'^next/three_(?P<name>\w+)$',views.three, name='three'),

    #水稻的下一级（三级）
    url(r'^next/pro_(?P<name>\w+)$', views.pro, name='pro'),

    #产品信息(四级)
    url(r'^info/(?P<name>\w+)/(?P<uid>\w+)$', views.info1, name='info1'),

    #人才战略
    url(r'^talent$', views.talent, name='talent'),

    #肥效展示
    url(r'^tech$', views.tech, name='tech'),

    #农友足迹
    url(r'^zuji$', views.zuji, name='zuji'),

    #人员描述
    url(r'^person$', views.person,name='person'),
]

handler404 = myweb.views.page_not_found