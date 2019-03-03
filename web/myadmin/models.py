from django.db import models

# Create your models here.
class nongyou(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    state = models.IntegerField(default=1)

# 三级表  SDzz = 水稻种子表
class SD_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_zz"

# 四级表  ZYJgzwhj = 种衣剂干籽丸化剂表
class SD_ZYJ_gzwhj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_zyj_gzwhj"
# 四级表 ZYJjzj = 种衣剂浸种剂表
class SD_ZYJ_jzj(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_zyj_jzj"
# 四级表 ZYJzzbyj = 种衣剂种子包衣剂表
class SD_ZYJ_zzbyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_zyj_zzbyj"
# 三级表 SDsyj = 水稻水秧剂表
class SD_syj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_syj"
# 三级表 SDzckdj = 水稻增产抗倒剂表
class SD_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_zckdj"
# 三级表 SDfhchf = 水稻复合掺混肥表
class SD_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_fhchf"
# 三级表 SDtcf = 水稻套餐肥表
class SD_tcf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_tcf"
# 三级表 SDfqf = 水稻返青肥表
class SD_fqf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_fqf"
# 三级表 SDhf = 水稻穗肥表
class SD_hf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_hf"

# 四级表 CCJdjccj = 除草剂打浆除草剂表
class SD_CCJ_djccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_djccj"
# 四级表 CCJybccj = 除草剂一遍除草剂表
class SD_CCJ_ybccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_ybccj"
# 四级表 CCJebccj = 除草剂二遍除草剂表
class SD_CCJ_ebccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_ebccj"
# 四级表 CCJympwccj = 除草剂叶面喷雾除草剂表
class SD_CCJ_ympwccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_ympwccj"
# 四级表 CCJptccj = 除草剂泡腾除草剂表
class SD_CCJ_ptccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_ptccj"
# 四级表 CCJptccj = 其他除草剂
class SD_CCJ_qtccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ccj_qtccj"
# 三级表 SDscj = 水稻杀虫剂表
class SD_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_scj"
# 三级表 SDsjj = 水稻杀菌剂表
class SD_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_sjj"
# 三级表 SDymf = 水稻叶面肥表
class SD_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_sd_ymf"

#------------------水稻相关表结束--------------------



#------------------农用物资相关表开始--------------------

# 三级表 NYWZnm = 农用物资农膜表
class NYWZ_nm(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_nywz_nm"
# 三级表 NYWZyp = 农用物资秧盘表
class NYWZ_yp(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_nywz_yp"
# 三级表 NYWZtp = 农用物资托盘表
class NYWZ_tp(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_nywz_tp"
# 三级表 NYWZdps = 农用物资大棚绳表
class NYWZ_dps(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_nywz_dps"
# 三级表 NYWZqt = 农用物资其他表
class NYWZ_qt(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_nywz_qt"


# ------------------农用物资相关表结束--------------------

# ------------------玉米相关表开始--------------------


# 三级表 YMzz = 玉米种子表
class YM_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_zz"

# 三级表 YMzyj = 玉米种衣剂表
class YM_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_zyj"

# 三级表 YMfhchf = 玉米复合掺混肥表
class YM_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_fhchf"

# 三级表 YMtxzf = 玉米特效追肥表
class YM_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_txzf"

# 三级表 YMlsy = 玉米老三样表
class YM_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_lsy"

# 三级表 YMccj = 玉米除草剂表
class YM_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_ccj"

# 三级表 YMscj = 玉米杀虫剂表
class YM_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_scj"

# 三级表 YMsjj = 玉米杀菌剂表
class YM_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_sjj"

# 三级表 YMzckdj = 玉米增产抗倒剂表
class YM_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_zckdj"

class YM_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_ym_ymf"

# ------------------玉米相关表结束--------------------


# ------------------高粱相关表开始--------------------


# 三级表 GLzz = 高粱种子表
class GL_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_zz"

# 三级表 GLzyj = 高粱种衣剂表
class GL_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_zyj"

# 三级表 GLfhchf = 高粱复合掺混肥表
class GL_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_fhchf"

# 三级表 GLtxzf = 高粱特效追肥表
class GL_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_txzf"

# 三级表 GLlsy = 高粱老三样表
class GL_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_lsy"

# 三级表 GLccj = 高粱除草剂表
class GL_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_ccj"

# 三级表 GLscj = 高粱杀虫剂表
class GL_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_scj"

# 三级表 GLsjj = 高粱杀菌剂表
class GL_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_sjj"

# 三级表 GLzckdj = 高粱增产抗倒剂表
class GL_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_zckdj"

class GL_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_gl_ymf"

# ------------------高粱相关表结束--------------------

# ------------------大豆相关表开始--------------------

# 三级表 DDzz = 大豆种子表
class DD_zz(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_zz"

# 三级表 DDzyj = 大豆种衣剂表
class DD_zyj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_zyj"

# 三级表 DDfhchf = 大豆复合掺混肥表
class DD_fhchf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_fhchf"

# 三级表 DDtxzf = 大豆特效追肥表
class DD_txzf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_txzf"

# 三级表 DDlsy = 大豆老三样表
class DD_lsy(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_lsy"

# 三级表 DDccj = 大豆除草剂表
class DD_ccj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_ccj"

# 三级表 DDscj = 大豆杀虫剂表
class DD_scj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_scj"

# 三级表 DDsjj = 大豆杀菌剂表
class DD_sjj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_sjj"

# 三级表 DDzckdj = 大豆增产抗倒剂表
class DD_zckdj(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_zckdj"

# 三级表 DDzckdj = 大豆增产抗倒剂表
class DD_ymf(models.Model):
    images = models.ImageField(upload_to='img')
    content = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    infoimg = models.ImageField(upload_to='img')
    class Meta:
        db_table = "myweb_dd_ymf"

# ------------------大豆相关表结束--------------------

# 员工查看 model 类
class work(models.Model):
    img = models.ImageField(upload_to='work')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    class Meta:
        db_table = "myweb_work"

#农友足迹 model类
class foot(models.Model):
    img = models.ImageField(upload_to='foot')
    href = models.CharField(max_length=100)
    class Meta:
        db_table = "myweb_foot"

#最新资讯
class news(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    class Meta:
        db_table = "myweb_news"