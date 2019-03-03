from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import re

class AdminMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # 定义网站后台不用登录也可访问的路由url
        urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout']
        # 获取当前请求路径
        path = request.path
        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match("/myadmin",path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "adminuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('myadmin_login'))
        response = self.get_response(request)
        return response