import requests
import xlrd
import random
import time
import os
import json

# 代理池的导入 (此处为付费!!!)
# def agent_ip():
#     pass
#     IP_URL = 'https://proxy.horocn.com/api/proxies?order_id=HISB1616617748301972&num=10&format=json&line_separator=win'
#     res = requests.get(IP_URL)
#     s = json.loads(res.text)
#     agent = []
#     for j in s:
#         IP = {'http': j['host'] + ':' + j['port'], 'https': j['host'] + ':' + j['port']}
#         agent.append(IP)
#     return agent
IP = [
{'http':'116.255.172.214:16816','https':'116.255.172.214:16816'},
# {'http':'116.255.169.214:16816','https':'116.255.172.169:16816'},
{'http':'116.255.189.171:16816','https':'116.255.189.171:16816'},
{'http':'116.255.197.58:16816','https':'116.255.197.58:16816'},
{'http':'42.51.28.155:16817','https':'42.51.28.155:16817'},
{'http':'116.255.177.231:16817','https':'116.255.177.231:16817'},
{'http':'42.51.40.241:16817','https':'42.51.40.241:16817'},
]

#变量的提取模块 从excel中拿出前两列的数据
def read_excel_xls(path):
    ps = []
    r = []
    workbook = xlrd.open_workbook('./ps-r.xlsx')  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    # 读取第一列
    for j in range(0, worksheet.nrows):# 从第1行开始读取到最终行
        if worksheet.cell_value(j,0) != '':
            ps.append(worksheet.cell_value(j,0))# 逐行逐列读取数据
    # 读取第二列
    for j in range(0, worksheet.nrows):
        if worksheet.cell_value(j,1) != '':
            r.append(worksheet.cell_value(j,1))
    return [ps,r]
def res_csv(url):
    global num,IP_time,IP,proxy_open,proxy
    while True:
        try:
            # if proxy_open==False:
            #     if IP_time >= 5:
            #         IP_time = 0
            #         IP = agent_ip()
            #         print('代理池更新ing,么么哒')
            proxy = random.choice(IP)
            header = random.choice(headers)
            print(proxy)
            if os.path.exists("./info_AG4/{0}+ps{1}+r{2}+rg{3}.csv".format(num,int(ps),int(r),rg)):
                print('文件已存在,无断点.跳过该文件')
                num += 1
                break
            else:
                response = requests.get(url,headers=header,timeout=10)#proxies=proxy,
                if response.status_code == 200:
                    print('正在以{0}的方式和IP为{1}的方式提取文件'.format(header,proxy))
                    with open("./info_AG4/{0}+ps{1}+r{2}+rg{3}.csv".format(num,int(ps),int(r),rg), 'wb') as f:
                        f.write(response.content)
                    print('文件提取完成')
                    size = os.path.getsize("./info_AG4/{0}+ps{1}+r{2}+rg{3}.csv".format(num,int(ps),int(r),rg))
                    if size >20000 or size ==611:
                        num += 1
                        time.sleep(1)
                        # proxy_open = True
                        break
                    else:
                        print('非611与真正的数据,重新爬取')
                        global errow
                        errow += 1
                        os.remove("./info_AG4/{0}+ps{1}+r{2}+rg1.csv".format(num,int(ps),int(r)))
                        print('移除当前文件,重新爬取')
                        if errow > 3:
                            errow = 0
                            break
                else:
                    pass
        except Exception as e:
            print(e)
            time.sleep(0.5)
            print('响应超时,重新选择代理池')
            # IP_time += 1
            # proxy_open = False
# 这其实是个文件名
num = 1
#代理池计时器
IP_time = 0
errow = 0
proxy_open = False
# 虚拟请求头导入
headers = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', },
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', },
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', },
    {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11', },
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)', },
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)', }
]
# 通过 ps-r 取值
tot_ps = read_excel_xls('ps-r.xlsx')[0][1:]
tot_r = read_excel_xls('ps-r.xlsx')[1][1:]
# 接口的制作
# IP = agent_ip() # 获取代理池
for rg in range(1,3):
    #改变国家
    for r in tot_r:
        #改变年份
        for ps in tot_ps:
            url = 'http://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps={0}&r={1}&p=0&rg={2}&cc=AG4&fmt=csv'.format(int(ps),int(r),rg)
            print(url)
            IP_time += 1
            if __name__ == '__main__':
                # 执行下载操作
                res_csv(url)







