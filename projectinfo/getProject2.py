import ast
import os
from datetime import datetime

import xlwt
from bs4 import  BeautifulSoup
from urllib.request import *
import urllib
import numpy as np

from random import randint
import re
import json
import requests
import time
# from selenium import webdriver
# 优青、杰青、重点、重大都要搞下来
# 按单位区分重名者
# 二维数组保存所有数据 最低维度保存为某个名字的专家的字典信息（可能有重名 所以可能有多个字典保存在一个列表中）
from selenium import webdriver

USER_AGENTS = [
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
                    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
                    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
                    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
                ]
# postUrl = "https://www.letpub.com.cn/nsfcfund_search.php?mode=advanced&datakind=list&currentpage=1"
postUrl = 'https://www.letpub.com.cn/nsfcfund_search.php?mode=advanced&datakind=excel&currentpage=1'
# authors = ['陈旭']

# projects = ['优秀青年基金项目','重点项目','重大项目','面上项目','国家杰出青年基金']
projects = ['国家杰出青年科学基金']

random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]



cookie = 'PHPSESSID=5blqprcin7a6b6lbljhffo1dm3; __utmt=1; __utma=189275190.1449889786.1653025996.1653025996.1653025996.1; __utmc=189275190; __utmz=189275190.1651222836.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=189275190.2.10.1653025996; _gat=1'
headers = {

    'User-Agent': random_agent,
    'Cookie':cookie,
    # 'Content-Disposition':'attachment;filename=testjhh.xls'
    # 'Host': 'apps.webofknowledge.com',
    # 'Upgrade-Insecure-Requests' : '1'

}
for project in projects:
    print(project)
    for i in range(1,8):

        lefturl = "&age=&name=&person=&no=&company=&addcomment_s1=F&addcomment_s2=F0"+(str)(i)+"&addcomment_s3=&addcomment_s4=&money1=&money2=&startTime=1997&endTime=2020&province_main=&subcategory=" + \
                  urllib.parse.quote(project) + "&searchsubmit=true"
        # req = Request(postUrl + lefturl, headers=headers)
        #
        # # req.encoding = req.apparent_encoding
        # # print(urls[0])
        # html = urlopen(req, timeout=10).read().decode('utf-8')
        #
        # # if i == 0:
        # #     print(html)
        # # print(html)
        # soup = BeautifulSoup(html, features='lxml')
        # tr = soup.find_all("tr")
        # university = ''
        # for i in tr:
        #     td = i.find_all("td")
        #     if len(td) == 0:
        #         continue
        #     if td[0].get_text() == '陈旭':
        #         if td[1].get_text() not in author_info:
        #             # print(1111111111111)
        #             university = td[1].get_text()
        #             author_info[td[1].get_text()] = {}
        #             author_info[td[1].get_text()]['project'] = 0
        #             author_info[td[1].get_text()]['subject'] = []
        #             author_info[td[1].get_text()]['code'] = []
        #         author_info[td[1].get_text()]['project'] += 1
        #     # print(td[0].get_text())
        #     if td[0].get_text() == '学科分类':
        #         author_info[university]['subject'].append(td[1].get_text())
        #     if td[0].get_text() == '学科代码':
        #         author_info[university]['code'].append(td[1].get_text())
        #
        #     # for td in td_all:
        # print(author_info)
        r = requests.post(postUrl + lefturl, headers=headers)
        time.sleep(10)
        data = r.json()
        if data['data'] == '':
            print('nothing')
            continue
        # print(data['data'])
        # # r = requests.get(r.json()['data'])
        # fp = open('test3.xls','wb')
        # fp.write(data['data'].encode(encoding='utf-8'))
        # fp.close()
        # r2 = requests.get(data['data'],headers)
        chrome_options = webdriver.ChromeOptions()

        prefs = {'profile.default_content_settings.popups': 0,  # 防止保存弹窗
                 'download.default_directory': 'D:\\authorData\\projectinfo\\xls\\',  # 设置默认下载路径
                 "profile.default_content_setting_values.automatic_downloads": 1  # 允许多文件下载
                 }
        chrome_options.add_experimental_option('prefs', prefs)

        # 修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(data['data'])
        # browser.close()
