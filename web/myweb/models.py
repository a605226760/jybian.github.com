from django.db import models

# 一级表  类别表  大的分类表
class One_Title(models.Model):
    TwoTitle = models.CharField(max_length=100)
    OneName = models.CharField(max_length=100)
    svg = models.CharField(max_length=20)

#------------------水稻相关表开始--------------------
# 二级表 SD = 水稻表
class SD(models.Model):
    TwoName = models.CharField(max_length=100)
    ThreeTitle = models.CharField(max_length=100)
    img =  models.CharField(max_length=100)
    svg = models.CharField(max_length=50)

# 三级表  SDzz = 水稻种子表
class SD_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表  SDzz = 水稻种衣剂表 --> 有四级表
class SD_zyj(models.Model):
    ThreeName = models.CharField(max_length=100)
    FourTitle = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

# 四级表  ZYJgzwhj = 种衣剂干籽丸化剂表
class SD_ZYJ_gzwhj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 ZYJjzj = 种衣剂浸种剂表
class SD_ZYJ_jzj(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    infoimg = models.ImageField(upload_to='img')

# 四级表 ZYJzzbyj = 种衣剂种子包衣剂表
class SD_ZYJ_zzbyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDsyj = 水稻水秧剂表
class SD_syj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDzckdj = 水稻增产抗倒剂表
class SD_zckdj(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDfhchf = 水稻复合掺混肥表
class SD_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDtcf = 水稻套餐肥表
class SD_tcf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDfqf = 水稻返青肥表
class SD_fqf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDhf = 水稻穗肥表
class SD_hf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDccj = 水稻除草剂表 --> 有四级表
class SD_ccj(models.Model):
    ThreeName = models.CharField(max_length=100)
    FourTitle = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

# 四级表 CCJdjccj = 除草剂打浆除草剂表
class SD_CCJ_djccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 CCJybccj = 除草剂一遍除草剂表
class SD_CCJ_ybccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 CCJebccj = 除草剂二遍除草剂表
class SD_CCJ_ebccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 CCJympwccj = 除草剂叶面喷雾除草剂表
class SD_CCJ_ympwccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 CCJptccj = 除草剂泡腾除草剂表
class SD_CCJ_ptccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 四级表 CCJqtccj = 其他除草剂
class SD_CCJ_qtccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDscj = 水稻杀虫剂表
class SD_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDsjj = 水稻杀菌剂表
class SD_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 SDymf = 水稻叶面肥表
class SD_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')


#------------------水稻相关表结束--------------------



#------------------农用物资相关表开始--------------------

# 二级表 NYWZ = 农用物资表
class NYWZ(models.Model):
    TwoName = models.CharField(max_length=100)
    ThreeTitle = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    svg = models.CharField(max_length=50)

# 三级表 NYWZnm = 农用物资农膜表
class NYWZ_nm(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 NYWZyp = 农用物资秧盘表
class NYWZ_yp(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 NYWZtp = 农用物资托盘表
class NYWZ_tp(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
# 三级表 NYWZdps = 农用物资大棚绳表
class NYWZ_dps(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 NYWZqt = 农用物资其他表
class NYWZ_qt(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')


# ------------------农用物资相关表结束--------------------


# ------------------玉米相关表开始--------------------

# 二级表 YM = 玉米表
class YM(models.Model):
    TwoName = models.CharField(max_length=100)
    ThreeTitle = models.CharField(max_length=1000)
    img = models.CharField(max_length=100)
    svg = models.CharField(max_length=20)

# 三级表 YMzz = 玉米种子表
class YM_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMzyj = 玉米种衣剂表
class YM_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMfhchf = 玉米复合掺混肥表
class YM_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMtxzf = 玉米特效追肥表
class YM_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMlsy = 玉米老三样表
class YM_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMccj = 玉米除草剂表
class YM_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMscj = 玉米杀虫剂表
class YM_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMsjj = 玉米杀菌剂表
class YM_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMzckdj = 玉米增产抗倒剂表
class YM_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 YMymf = 玉米叶面肥表
class YM_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')


# ------------------玉米相关表结束--------------------


# ------------------高粱相关表开始--------------------

# 二级表 GL = 高粱表
class GL(models.Model):
    TwoName = models.CharField(max_length=100)
    ThreeTitle = models.CharField(max_length=1000)
    img = models.CharField(max_length=100)
    svg = models.CharField(max_length=20)

# 三级表 GLzz = 高粱种子表
class GL_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLzyj = 高粱种衣剂表
class GL_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLfhchf = 高粱复合掺混肥表
class GL_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLtxzf = 高粱特效追肥表
class GL_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLlsy = 高粱老三样表
class GL_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLccj = 高粱除草剂表
class GL_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLscj = 高粱杀虫剂表
class GL_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLsjj = 高粱杀菌剂表
class GL_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLzckdj = 高粱增产抗倒剂表
class GL_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 GLymf = 高粱叶面肥
class GL_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')


# ------------------高粱相关表结束--------------------


# ------------------大豆相关表开始--------------------

# 二级表 DD = 大豆表
class DD(models.Model):
    TwoName = models.CharField(max_length=100)
    ThreeTitle = models.CharField(max_length=1000)
    img = models.CharField(max_length=100)
    svg = models.CharField(max_length=20)

# 三级表 DDzz = 大豆种子表
class DD_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDzyj = 大豆种衣剂表
class DD_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDfhchf = 大豆复合掺混肥表
class DD_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDtxzf = 大豆特效追肥表
class DD_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDlsy = 大豆老三样表
class DD_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDccj = 大豆除草剂表
class DD_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDscj = 大豆杀虫剂表
class DD_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDsjj = 大豆杀菌剂表
class DD_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDzckdj = 大豆增产抗倒剂表
class DD_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# 三级表 DDymf = 大豆叶面肥表
class DD_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')

# ------------------大豆相关表结束--------------------

# 员工查看 model 类
class work(models.Model):
    img = models.ImageField(upload_to='work')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    area = models.CharField(max_length=100)

#农友足迹 model类
class foot(models.Model):
    img = models.ImageField(upload_to='foot')
    href = models.CharField(max_length=100)

# 火爆热销
class hot(models.Model):
    images = models.ImageField(upload_to='hot')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='hot')

#最新资讯
class news(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)