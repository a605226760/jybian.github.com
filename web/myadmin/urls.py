from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name="myadmin_index"),
    url(r'^users$',views.usersindex,name="myadmin_uindex"),
    url(r'^usersadd$',views.usersadd,name="myadmin_add"),
    url(r'^usersinsert',views.usersinsert,name="myadmin_usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="myadmin_usersdel"),
    url(r'^users/(?P<uid>[0-9]+)/edit$', views.editUsers, name="myadmin_edit"), #加载用户信息编辑表单
    url(r'^users/update$', views.updateUsers, name="updateusers"),
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),
    url(r'^product/(?P<info>\w+)$',views.products, name="myadmin_products"),
    url(r'^product/(?P<uid>[0-9]+)/(?P<info>\w+)/bianji$', views.bianji, name="myadmin_bianji"),
    url(r'^product/(?P<uid>[0-9]+)/(?P<info>\w+)/update$', views.updateproduct, name="update_product"),
    url(r'^prodel/(?P<uid>[0-9]+)/(?P<info>\w+)$', views.prodel, name="myadmin_prodel"),
    url(r'^productadds/(?P<info>\w+)$',views.productadds,name="myadmin_adds"),
    url(r'^proadd/(?P<info>\w+)$',views.addplus,name="addplus"),
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~这里员工个人描述的表的增删查改处理系统~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 查看
    url(r'^works$',views.workindex,name="myadmin_work"),
    url(r'^worksadd$',views.workadd,name="myadmin_workadd"),
    url(r'^worksinsert$',views.workinsert,name="myadmin_workinsert"),
    url(r'^workdel/(?P<uid>[0-9]+)$', views.workdel, name="myadmin_workdel"),
    url(r'^workedit/(?P<uid>[0-9]+)$', views.editwork, name="myadmin_workedit"),
    url(r'^workedit/update$', views.updatework, name="myadmin_updatework"),

    #农友足迹
    url(r'^foot$', views.footindex, name="myadmin_foot"),
    url(r'^footadd$',views.footadd,name="myadmin_footadd"),
    url(r'^footinsert$', views.footinsert, name="myadmin_footinsert"),
    url(r'^fooedel/(?P<uid>[0-9]+)$', views.footdel, name="myadmin_footdel"),
    url(r'^footedit/(?P<uid>[0-9]+)$', views.editfoot, name="myadmin_footedit"),
    url(r'^footedit/update$', views.updatefoot, name="myadmin_updatefoot"),

    #火爆热销
    url(r'^hot$', views.hotindex, name="myadmin_hot"),
    url(r'^hotadd$',views.hotadd,name="myadmin_hotadd"),
    url(r'^hotinsert$', views.hotinsert, name="myadmin_hotinsert"),
    url(r'^hotdel/(?P<uid>[0-9]+)$', views.hotdel, name="myadmin_hotdel"),
    url(r'^hotedit/(?P<uid>[0-9]+)$', views.edithot, name="myadmin_hotedit"),
    url(r'^hotedit/update$', views.updatehot, name="myadmin_updatehot"),

    #最新资讯
    url(r'^news$', views.newsindex, name="myadmin_news"),
    url(r'^newsadd$',views.newsadd, name="myadmin_newsadd"),
    url(r'^newsinsert$', views.newsinsert, name="myadmin_newsinsert"),
    url(r'^newsdel/(?P<uid>[0-9]+)$', views.newsdel, name="myadmin_newsdel"),
    url(r'^newsedit/(?P<uid>[0-9]+)$', views.editnews, name="myadmin_newsedit"),
    url(r'^newsedit/update$', views.updatenews, name="myadmin_updatenews"),
]