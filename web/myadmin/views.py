from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import nongyou
from django.core.paginator import Paginator
import time,json
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import re
import os



#-----------------------------导入一级大类model---------------------------#
from myweb.models import One_Title

#-----------------------------导入二级类model---------------------------#
#水稻
from myweb.models import SD
#农用物资
from myweb.models import NYWZ
#玉米
from myweb.models import YM
#高粱
from myweb.models import GL
#大豆
from myweb.models import DD



#-----------------------------导入三级水稻类model---------------------------#

from myweb.models import SD_zz
from myweb.models import SD_zyj
from myweb.models import SD_syj
from myweb.models import SD_zckdj
from myweb.models import SD_fhchf
from myweb.models import SD_fqf
from myweb.models import SD_tcf
from myweb.models import SD_hf
from myweb.models import SD_ccj
from myweb.models import SD_scj
from myweb.models import SD_sjj
from myweb.models import SD_ymf

#-----------------------------导入三级玉米类model---------------------------#

from myweb.models import YM_zz
from myweb.models import YM_zyj
from myweb.models import YM_fhchf
from myweb.models import YM_txzf
from myweb.models import YM_lsy
from myweb.models import YM_ccj
from myweb.models import YM_scj
from myweb.models import YM_sjj
from myweb.models import YM_zckdj
from myweb.models import YM_ymf


#-----------------------------导入三级高粱类model---------------------------#

from myweb.models import GL_zz
from myweb.models import GL_zyj
from myweb.models import GL_fhchf
from myweb.models import GL_txzf
from myweb.models import GL_lsy
from myweb.models import GL_ccj
from myweb.models import GL_scj
from myweb.models import GL_sjj
from myweb.models import GL_zckdj
from myweb.models import GL_ymf


#-----------------------------导入三级大豆model---------------------------#
from myweb.models import DD_zz
from myweb.models import DD_zyj
from myweb.models import DD_fhchf
from myweb.models import DD_txzf
from myweb.models import DD_lsy
from myweb.models import DD_ccj
from myweb.models import DD_scj
from myweb.models import DD_sjj
from myweb.models import DD_zckdj
from myweb.models import DD_ymf


#-----------------------------导入三级农用物资model---------------------------#
from myweb.models import NYWZ_nm
from myweb.models import NYWZ_yp
from myweb.models import NYWZ_tp
from myweb.models import NYWZ_dps
from myweb.models import NYWZ_qt


#-----------------------------导入四级水稻种衣剂model---------------------------#
from myweb.models import SD_ZYJ_gzwhj
from myweb.models import SD_ZYJ_jzj
from myweb.models import SD_ZYJ_zzbyj


#-----------------------------导入四级水稻除草剂model---------------------------#
from myweb.models import SD_CCJ_djccj
from myweb.models import SD_CCJ_ybccj
from myweb.models import SD_CCJ_ebccj
from myweb.models import SD_CCJ_ympwccj
from myweb.models import SD_CCJ_ptccj
from myweb.models import SD_CCJ_qtccj
#-----------------------------业务员管理model---------------------------#
from myweb.models import work
from myweb.models import foot
from myweb.models import hot
from myweb.models import news




#后台首页
def index(request):
    return render(request,'myadmin/index.html')

def usersindex(request):
    lists = nongyou.objects.all()
    context = {'userlist':lists}
    return render(request,'myadmin/users/index.html',context)

def usersadd(request):
    return render(request,'myadmin/users/add.html')

def usersinsert(request):
    try:
        ob=nongyou()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.passwd = m.hexdigest()
        ob.phone = request.POST['phone']
        ob.addtime = time.time()
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as e:
        context = {'info': e}
    return render(request, "myadmin/infouser.html", context)

def usersdel(request,uid):
    try:
        ob=nongyou.objects.get(id=uid)
        ob.delete()
        context={'info':'删除成功'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/infouser.html",context)

# 加载信息编辑表单
def editUsers(request,uid):
    try:
        ob = nongyou.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/users/edit.html",context)
    except Exception as e:
        context = {'info':e}
        return render(request,"myadmin/infouser.html",context)

def updateUsers(request):
    try:
        ob = nongyou.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/infouser.html",context)

# 会员登录表单
def login(request):
    return render(request,'myadmin/login.html')

# 会员执行登录
def dologin(request):
    try:
        #根据账号获取登录者信息
        user = nongyou.objects.get(username=request.POST['username'])

        # 验证密码
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        if user.passwd == m.hexdigest():
        # 此处登录成功，将当前登录信息放入到session中，并跳转页面
            request.session['adminuser'] = user.name
            return redirect(reverse('myadmin_index'))
        else:
            context = {'info':'登录密码错误！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myadmin/login.html",context)
# 会员退出
def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('myadmin_login'))
    # 加载登录页面(url地址不变)


#浏览商品
def products(request,info):
    dict_info = {
        #水稻
        'SD_zz':'水稻种子表',
        'SD_ZYJ_gzwhj' : '水稻种衣剂干籽丸化剂表',
        'SD_ZYJ_jzj': '水稻种衣剂浸种剂表',
        'SD_ZYJ_zzbyj' : '水稻种衣剂种子包衣剂表',
        'SD_syj':'水稻壮秧剂表',
        'SD_zckdj': '水稻增产抗倒剂表',
        'SD_fhchf' : '水稻复合掺混肥表',
        'SD_tcf' : '水稻套餐肥表',
        'SD_fqf':'水稻返青肥表',
        'SD_hf' : '水稻穗肥表',
        'SD_CCJ_djccj' : '水稻除草剂打浆除草剂表',
        'SD_CCJ_ybccj' : '水稻除草剂一遍除草剂表',
        'SD_CCJ_ebccj' : '水稻除草剂二遍除草剂表',
        'SD_CCJ_ympwccj' : '水稻除草剂叶面喷雾除草剂表',
        'SD_CCJ_ptccj' : '水稻除草剂泡腾除草剂表',
        'SD_CCJ_qtccj': '水稻除草剂其他除草剂表',
        'SD_scj':'水稻杀虫剂表',
        'SD_sjj' :'水稻杀菌剂表',
        'SD_ymf' : '水稻叶面肥表',
        #农用物资
        'NYWZ_nm' : '农用物资农膜表',
        'NYWZ_yp': '农用物资秧盘表',
        'NYWZ_tp' : '农用物资托盘表',
        'NYWZ_dps' : '农用物资大棚绳表',
        'NYWZ_qt' : '农用物资其他表',
        #玉米
        'YM_zz' : '玉米种子表',
        'YM_zyj' :'玉米种衣剂表',
        'YM_fhchf' : '玉米复合掺混肥表',
        'YM_txzf' : '玉米特效追肥表',
        'YM_lsy' : '玉米老三样表',
        'YM_ccj' : '玉米除草剂表',
        'YM_scj' : '玉米杀虫剂表',
        'YM_sjj' :'玉米杀菌剂表',
        'YM_zckdj':'玉米增产抗倒剂表',
        'YM_ymf': '玉米叶面肥表',
        #高粱
        'GL_zz' : '高粱种子表',
        'GL_zyj': '高粱种衣剂表',
        'GL_fhchf': '高粱复合掺混肥表',
        'GL_txzf': '高粱特效追肥表',
        'GL_lsy': '高粱老三样表',
        'GL_ccj': '高粱除草剂表',
        'GL_scj': '高粱杀虫剂表',
        'GL_sjj': '高粱杀菌剂表',
        'GL_zckdj': '高粱增产抗倒剂表',
        'GL_ymf': '高粱叶面肥表',
        #大豆
        'DD_zz': '大豆种子表',
        'DD_zyj': '大豆种衣剂表',
        'DD_fhchf': '大豆复合掺混肥表',
        'DD_txzf': '大豆特效追肥表',
        'DD_lsy': '大豆老三样表',
        'DD_ccj': '大豆除草剂表',
        'DD_scj': '大豆杀虫剂表',
        'DD_sjj': '大豆杀菌剂表',
        'DD_zckdj': '大豆增产抗倒剂表',
        'DD_ymf': '大豆叶面肥表',
  }
    try:
        s = eval(info).objects.all()
        name_pro = dict_info[str(info)]
        context = {'prolist': s,'info':info,'namepro':name_pro}
        return render(request, 'myadmin/product/products.html',context)
    except:
        context = {'info': '服务器开小差了,请重新操作'}
        return render(request, "myadmin/info.html", context)

#编辑
def bianji(request,uid,info):
    ob = eval(info).objects.get(id=uid)
    context = {'prolist':ob,'info':info}
    return render(request,'myadmin/product/bianji1.html',context)
# 编辑更新
def updateproduct(request,uid,info):
    try:
        ob =eval(info).objects.get(id=uid)
        # 进行产品缩略小图的上传与删除
        try:
            cc = request.FILES['images']
            try:
                delurl = '/NyDjango/farm/media/' + str(ob.images)
                os.remove(delurl)
            except:
                pass
            try:
                ob.images = request.FILES['images']
            except:
                pass
            try:
                ob.images = cc
            except:
                pass
        except:
            pass
        # 进行详细长图片的上传与删除
        try:
            cc = request.FILES['infoimg']
            try:
                delurl = '/NyDjango/farm/media/' + str(ob.infoimg)
                os.remove(delurl)
            except:
                pass
            try:
                ob.infoimg = request.FILES['infoimg']
            except:
                pass
            try:
                ob.infoimg = cc
            except:
                pass
        except:
            pass
        ob.name = request.POST['name']
        ob.content = request.POST['content']
        ob.save()
        context = {'info':'修改成功！','luyourt':info}
    except:
        context = {'info':'修改失败！请检查图片是否上传,以及信息是否填写'}
    return render(request,"myadmin/info.html",context)



#产品信息删除
def prodel(request,uid,info):
    try:
        ob=eval(info).objects.get(id=uid)
        # 拼接数据库中图片路径 执行删除操作
        try:
            delurl = '/NyDjango/farm/media/'+str(ob.images)
            os.remove(delurl)
        except:
            pass
        # 拼接数据库中图片路径 执行详情页面的长图删除操作
        try:
            delurl2 = '/NyDjango/farm/media/'+str(ob.infoimg)
            os.remove(delurl2)
        except:
            pass
        ob.delete()
        context={'info':'删除成功','luyourt':info}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 产品信息添加页面
def productadds(request,info):
    content = {'info':info}
    return render(request, 'myadmin/product/adds.html',content)

# 产品信息添加操作
def addplus(request,info):
    try:
        ob =eval(info)()
        try:
            ob.images = request.FILES['images']
        except:
            pass
        try:
            ob.infoimg = request.FILES['infoimg']
        except:
            pass
        ob.name = request.POST['name']
        ob.content = request.POST['content']
        ob.save()
        context = {'info':'添加成功！','luyourt':info}
    except:
        context = {'info':'添加失败！请检查图片是否上传,以及信息是否填写'}
    return render(request,"myadmin/info.html",context)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~这里员工个人描述的表的增删查改处理系统~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def workindex(request):
    lists = work.objects.all()
    context = {'userlist': lists}
    return render(request, 'myadmin/work/workindex.html', context)
def workadd(request):
    return render(request,'myadmin/work/workadd.html')
def workinsert(request):
    try:
        ob=work()
        ob.name = request.POST['name']
        ob.phone = request.POST['phone']
        ob.area = request.POST['area']
        try:
            ob.img = request.FILES['img']
        except:
            pass
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as e:
        context = {'info': e}
    return render(request, "myadmin/infowork.html", context)

def workdel(request,uid):
    try:
        ob=work.objects.get(id=uid)
        try:
            delurl = '/NyDjango/farm/media/' + str(ob.img)
            os.remove(delurl)
        except:
            pass
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/infowork.html",context)
# 加载信息编辑表单
def editwork(request,uid):
    try:
        ob = work.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/work/edit.html",context)
    except Exception as e:
        context = {'info':e}
        return render(request,"myadmin/infowork.html",context)

def updatework(request):
    try:
        ob = work.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.phone = request.POST['phone']
        ob.area = request.POST['area']
        try:
            delurl = '/NyDjango/farm/media/' + str(ob.img)
            os.remove(delurl)
        except:
            pass
        try:
            ob.img = request.FILES['img']
        except:
            pass
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/infowork.html",context)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~这里农友足迹的表的增删查改处理系统~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def footindex(request):
    lists = foot.objects.all()
    context = {'userlist': lists}
    return render(request, 'myadmin/foot/footindex.html', context)

def footadd(request):
    return render(request,'myadmin/foot/footadd.html')
def footinsert(request):
    try:
        ob=foot()
        try:
            ob.img = request.FILES['img']
        except:
            pass
        ob.href = request.POST['href']
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as e:
        context = {'info': e}
    return render(request, "myadmin/infofoot.html", context)

def footdel(request,uid):
    try:
        ob=foot.objects.get(id=uid)
        try:
            delurl = '/NyDjango/farm/media/' + str(ob.img)
            os.remove(delurl)
        except:
            pass
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/infofoot.html",context)

# 加载信息编辑表单
def editfoot(request,uid):
    try:
        ob = foot.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/foot/edit.html",context)
    except Exception as e:
        context = {'info':e}
        return render(request,"myadmin/infofoot.html",context)

def updatefoot(request):
    try:
        ob = foot.objects.get(id=request.POST['id'])
        ob.href = request.POST['href']
        try:
            ss = request.FILES['img']
            try:
                delurl = '/NyDjango/farm/media/' + str(ob.img)
                os.remove(delurl)
            except:
                pass
            try:
                ob.img = ss
            except:
                pass
        except:
            pass
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/infofoot.html",context)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~这里火爆热销的表的增删查改处理系统~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def hotindex(request):
    lists = hot.objects.all()
    context = {'userlist': lists}
    return render(request, 'myadmin/hot/hotindex.html', context)

def hotadd(request):
    return render(request,'myadmin/hot/hotadd.html')
def hotinsert(request):
    try:
        ob = hot()
        try:
            ob.images = request.FILES['images']
        except:
            pass
        try:
            ob.infoimg = request.FILES['infoimg']
        except:
            pass
        ob.name = request.POST['name']
        ob.content = request.POST['content']
        ob.save()
        context = {'info': '添加成功！'}
    except:
        context = {'info': '添加失败！请检查图片是否上传,以及信息是否填写'}
    return render(request, "myadmin/infohot.html", context)

def hotdel(request,uid):
    try:
        ob=hot.objects.get(id=uid)
        try:
            delurl = '/NyDjango/farm/media/' + str(ob.img)
            os.remove(delurl)
        except:
            pass
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/infohot.html",context)

# 加载信息编辑表单
def edithot(request,uid):
    try:
        ob = hot.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/hot/hotedit.html",context)
    except Exception as e:
        context = {'info':e}
        return render(request,"myadmin/infohot.html",context)

def updatehot(request):
    try:
        ob = hot.objects.get(id=request.POST['id'])
        ob.name = request.POST['name']
        ob.content = request.POST['content']
        # 进行产品缩略小图的上传与删除
        try:
            cc = request.FILES['images']
            try:
                delurl = '/NyDjango/farm/media/' + str(ob.images)
                os.remove(delurl)
            except:
                pass
            try:
                ob.images = cc
            except:
                pass
        except:
            pass

        # 进行详细长图片的上传与删除
        try:
            cc = request.FILES['infoimg']
            try:
                delurl = '/NyDjango/farm/media/' + str(ob.infoimg)
                os.remove(delurl)
            except:
                pass
            try:
                ob.infoimg = request.FILES['infoimg']
            except:
                pass
            try:
                ob.infoimg = cc
            except:
                pass
        except:
            pass
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！请检查图片是否上传,以及信息是否填写'}
    return render(request,"myadmin/infohot.html",context)


def page_not_found(request):
    context = {'info': '子链接不存在,请检查链接是否正确'}
    return render('info.html',context)

def page_error(request):
    context = {'info': '操作异常,请按照正常操作方式管理'}
    return render('info.html', context)

def permission_denied(request):
    context = {'info': '图片不存在!'}
    return render('info.html', context)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~这里最新资讯的表的增删查改处理系统~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def newsindex(request):
    lists = news.objects.all()
    context = {'newslist': lists}
    return render(request, 'myadmin/news/newsindex.html', context)

def newsadd(request):
    return render(request, 'myadmin/news/newsadd.html')

def newsinsert(request):
    try:
        ob = news()
        ob.title = request.POST['title']
        ob.content = request.POST['content']
        ob.save()
        context = {'info': '添加成功！'}
    except:
        context = {'info': '添加失败！请检查信息是否填写'}
    return render(request, "myadmin/infonews.html",context)

def newsdel(request,uid):
    try:
        ob=news.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/infonews.html",context)


def editnews(request,uid):
    try:
        ob = news.objects.get(id=uid)
        context = {'news':ob}
        return render(request,"myadmin/news/newsedit.html",context)
    except Exception as e:
        context = {'info':e}
        return render(request,"myadmin/infonews.html",context)

def updatenews(request):
    try:
        ob = news.objects.get(id=request.POST['id'])
        ob.title = request.POST['title']
        ob.content = request.POST['content']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/infonews.html",context)
