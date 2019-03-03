from __future__ import unicode_literals
from wxpy import Bot
import time
import random

def works(info):
    my_friend = bot.groups().search(u'你不热啊？')[0]
    my_friend.send('@所有人\n'
                   '丨---------每日播报-------丨\n'
                   '丨-----------{0}-----------丨\n'
                   '丨-----------{0}-----------丨\n'
                   '丨-----------{0}-----------丨\n'
                   '丨-----------{0}-----------丨\n'
                   '丨-----------{0}-----------丨\n'
                   '丨---------播报完毕-------丨\n'.format(info)
                   )
    time.sleep(3600)
bot = Bot(console_qr=2,cache_path="botoo.pkl")
while True:
    try:
        times = time.strftime('%Hh:%Mm:%S',time.localtime(time.time()))
        #获取今天是星期几
        weekday = int(time.strftime('%w',time.localtime(time.time())))
        # 每天 13:00 押镖 && 周日 13:00 光明顶 && 周四 13:00 帮战合成武器
        if '13h:' in times:
            if weekday == 0:
                works('押镖+光明顶BOSS战！')
            elif weekday == 4:
                works('押镖+帮战合武器！')
            else:
                works('押镖')
        # 周一到周六 12:00 光明顶 周三周五 12:00大乱斗
        if '12h' in times:
            if weekday<=6 and weekday!=0:
                if weekday==3 or weekday==5:
                    works('光明顶+大乱斗')
                else:
                    works('光明顶')
            if weekday==0:
                works('华山论剑助威')
        if weekday==0 and '21h' in times:
            works('组队大乱斗+光明顶领取奖励！')
        if weekday== 3 or weekday == 5:
            if '21h' in times:
                works('大乱斗')
        if '22h' in times:
            works('押镖')
        if '11h' in times:
            works('每日闹钟+便当')
        if '16h' in times:
            works('闹钟响了')
        if '19h' in times:
            works('闹钟响了')
        if '18h' in times:
            works('便当开饭啦！')
    except Exception as e:
        print('程序出错了！！！！'+str(e))
    time.sleep(10)

