from django.shortcuts import render
from django.shortcuts import HttpResponse


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

from myweb.models import work
from myweb.models import foot
from myweb.models import hot
from myweb.models import news






#------------------------PC端开始-----------------------#
# pc端主页视图
def index(request):
    s = hot.objects.all()
    new = news.objects.all()
    context = {'prolist':s,'new':new}
    return render(request,'myweb/index.html',context)

# 关于我们视图
def about(request):
    return render(request, 'myweb/pcweb/about.html')

# 联系我们视图
def contact(request):
    return render(request, 'myweb/pcweb/contact.html')

# 产品展示默认视图
def product_list(request):
    s = One_Title.objects.all()
    y = SD.objects.all()
    context = {'productlist':s,'productlist_2':y}
    return render(request, 'myweb/pcweb/product_list.html',context)

# 产品展示
def product_lists(request,name):
    s = One_Title.objects.all()
    y = eval(name).objects.all()
    context = {'productlist':s,'productlist_2':y}
    return render(request, 'myweb/pcweb/product_list.html',context)

# 产品展示下二级列表视图
def yumi(request,name):
    ss = eval(name).objects.all()
    ssrrzz = ''
    try:
        for i in ss:
            res = i.id
            ssrrzz = eval(name).objects.get(id=res)
            break
    except:
        pass

    # productlists 表的id数据
    # productlist 表的全部数据
    context = {'productlist': ss,'name':name,'productlists': ssrrzz}
    list_three = ['SD_zyj', 'SD_ccj']
    if name in list_three:
        return render(request, 'myweb/pcweb/yumi.html',context)
    else:
        return render(request, 'myweb/pcweb/product_info.html',context)

# 产品信息详情
def product_info(request,uid,name):
    s = eval(name).objects.get(id=uid)
    ss = eval(name).objects.all()
    # productlists 表的id数据
    # productlist 表的全部数据
    context = {'productlist': ss,'productlists': s,'name':name}
    return render(request, 'myweb/pcweb/product_info.html',context)

def error(request):
    return render(request, 'myweb/pcweb/error.html')
#新闻
# pc端主页视图
def new_info(request):
    # s = nongyou.objects.all()
    # context = {'prolist':s}
    return render(request,'myweb/pcweb/new_info.html')


#------------------------PC端结束-----------------------#

#------------------------app端开始-----------------------#
#集团简介
def introduce(request):
    return render(request,'myweb/appweb/introduce.html')

#核心技术
def jishu(request):
    return render(request,'myweb/appweb/news.html')

#产品中心（一级大类）
def product(request):
    s = One_Title.objects.all()
    context = {'productlist':s}
    return render(request,'myweb/appweb/product.html',context)

#水稻（二级）
def shuidao(request,name):
    s = eval(name).objects.all()
    context = {'productlist':s}

    return render(request,'myweb/appweb/product_shuidao.html',context)

#三级文件夹
def three(request,name):
    #-----yes-----
    s = eval(name).objects.all()
    context = {'productlist':s,'name':name}
    list_three = ['SD_zyj', 'SD_ccj']
    if name in list_three:
        return render(request, 'myweb/appweb/sd_three1.html', context)
    else:
        return render(request,'myweb/appweb/sd_pro.html',context)

#（四级）
def pro(request,name):
    s = eval(name).objects.all()
    context = {'productlist': s,'name':name}
    return render(request,'myweb/appweb/sd_pro.html',context)

#产品信息（五级）
def info1(request,name,uid):
    s = eval(name).objects.get(id=uid)
    context = {'productlist': s}
    return render(request,'myweb/appweb/info.html',context)

#人才战略
def talent(request):
    return render(request,'myweb/appweb/talent.html')

#肥效展示
def tech(request):
    return render(request,'myweb/appweb/tech.html')

#农友足迹
def zuji(request):
    ob = foot.objects.all()
    context = {'info': ob}
    return render(request,'myweb/appweb/zuji.html',context)

#人员描述
def person(request):
    ob = work.objects.all()
    context = {'info':ob}
    return render(request,'myweb/appweb/person.html',context)
#------------------------app端结束-----------------------#

#404
def page_not_found(request):
    return render('404.html')

def page_error(request):
    return render(request, '500.html')

def permission_denied(request):
    return render(request, '403.html')
# def uploadImg(request): # 图片上传函数
#     if request.method == 'POST':
#         img = Img(img_url=request.FILES.get('img'))
#         img.save()
#     return render(request, 'imgupload.html')
