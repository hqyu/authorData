import json
import os
import re
import time
import urllib
from random import randint
from urllib.request import Request, urlopen
import pandas as pd
from glob import glob
import numpy as np
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
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
postUrl = 'https://www.letpub.com.cn/nsfcfund_search.php?mode=advanced&datakind=list&currentpage=1'
cookie = '__utmz=189275190.1651222836.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.3.1449889786.1653025996; _gid=GA1.3.1449480237.1653298986; PHPSESSID=1gue35uvnoup88aapkorupka95; __utma=189275190.1449889786.1653025996.1653298992.1653354031.11; __utmc=189275190; __utmt=1; Hm_lvt_a94e857ae4207c3ac8fcfd63f6604f22=1653150719,1653184768,1653298986,1653354031; Hm_lpvt_a94e857ae4207c3ac8fcfd63f6604f22=1653354042; __utmb=189275190.10.10.1653354031'
random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
headers = {

    'User-Agent': random_agent,
    'Cookie':cookie,
    'Connection': 'close'
    # 'Content-Disposition':'attachment;filename=testjhh.xls'
    # 'Host': 'apps.webofknowledge.com',
    # 'Upgrade-Insecure-Requests' : '1'

}
proxy_list = [
'182.39.6.245:38634',
'115.210.181.31:34301',
'123.161.152.38:23201',
'222.85.5.187:26675',
'123.161.152.31:23127',
]
ids = np.load('ids2.npy')
types = ['优秀青年基金项目','重点项目','重大项目','国家杰出青年科学基金','面上项目','重大研究计划','联合基金项目']
length = len(ids)
with open('professors2.json', 'r', encoding='utf-8')as f:
    xiugai = json.load(f)
num = 0
for id in ids:
    num+=1
    name = id.split("_")[0]
    university = id.split("_")[1]
    # xiugai[id]['面上项目']={}
    for t in types:
        lefturl = "&age=&name=&person="+urllib.parse.quote(name)+"&no=&company="+urllib.parse.quote(university)+"&addcomment_s1=&addcomment_s2=&addcomment_s3=&addcomment_s4=&money1=&money2=&startTime=1997&endTime=2020&province_main=&subcategory=" + \
                  urllib.parse.quote(t) + "&searchsubmit=true"
        req = Request(postUrl + lefturl, headers=headers)

        # req.encoding = req.apparent_encoding
        # print(urls[0])
        while True:
            try:

                html = urlopen(req, timeout=10).read().decode('utf-8')
                break
            except:
                time.sleep(10)
                print('error')
                print(id,t)
        time.sleep(5)
        soup = BeautifulSoup(html, features='html.parser')
        # print(soup)
        b = soup.find("b")
        if b == None:
            xiugai[id][t]['num'] = 0
            print(num, '/', length)
            continue
        xiugai[id][t]['num']=b.get_text()
        tr = soup.find_all("tr")
        # university = ''
        info = {}
        infos=[]
        for i in tr:
            td = i.find_all("td")
            if len(td) == 0:
                continue
            # info = {}
            if td[0].get_text() == name:
                info = {}
                info['project_id']=td[3].get_text()
                info['money']=td[2].get_text()
                info['accepted']=td[6].get_text()
            if td[0].get_text() == '题目':
                info['title'] = td[1].get_text()
            if td[0].get_text() == '执行时间':
                s=td[1].get_text().split("至")
                if len(s) == 0:
                    info['start'] = 'false'
                    info['end'] = 'false'
                if len(s) == 2:
                    info['start'] = s[0]
                    info['end'] = s[1]
                    infos.append(info)
            if td[0].get_text() == '学科代码':
                b = re.findall('一级：(.*)二级：', td[1].get_text())
                if len(b) == 0:
                    info['one'] = ''
                else:
                    info['one'] = b[0]
                b = re.findall('二级：(.*)三级：', td[1].get_text())
                if len(b) == 0:
                    info['two'] = ''
                else:
                    info['two'] = b[0]
                b = td[1].get_text().split(":")
                if b[-1][-2:] == '三级':
                    info['three'] = ''
                else:
                    print(b[-1][-2:])
                    info['three'] = b[-1]

        xiugai[id][t]["info"]=infos
        # print(divs)
        # for div in divs:
        #     b = div.find('b')
        #     print(b)
        # try:
        # r = requests.post(postUrl + lefturl, headers=headers)
        #
        # try:
        #
        #     data = r.json()
        # except requests.exceptions.JSONDecodeError as e:
        #     print('wait....')
        #     time.sleep(60)
        #     r = requests.post(postUrl + lefturl, headers=headers)
        #     try:
        #         data = r.json()
        #     except requests.exceptions.JSONDecodeError as e:
        #         print('wait longer...')
        #         time.sleep(300)
        #         r = requests.post(postUrl + lefturl, headers=headers)
        #         data = r.json()
        # chrome_options = webdriver.ChromeOptions()
        #
        # prefs = {'profile.default_content_settings.popups': 0,  # 防止保存弹窗
        #          'download.default_directory': 'D:\\authorData\\projectinfo\\xls2\\',  # 设置默认下载路径
        #          "profile.default_content_setting_values.automatic_downloads": 1  # 允许多文件下载
        #          }
        # chrome_options.add_experimental_option('prefs', prefs)
        #
        # # 修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #
        # browser = webdriver.Chrome(chrome_options=chrome_options)
        # print(postUrl+lefturl)
        # if data['data'] == '':
        #     print(num, '/', len(ids)-2)
        #     continue
        # browser.get(data['data'])
        # time.sleep(5)
        # browser.close()
        # files = sorted(glob('./xls2/*.xls'))
        # author_info = {}

        # # print(files)
        # names = ['项目标题', '所属学部', '项目类型', '项目编号', '金额', '负责人', '单位', '批准年份', '执行起自', '执行截至']
        # # types = ['优秀青年基金项目','重点项目','重大项目','面上项目']
        # # ids=[]
        # t = "面上项目"
        # for file in files:
        #
        #     df = pd.read_excel(file, header=None, names=names)
        #     df = df.drop(index=0)
        #     df = df.drop(index=1)
        #     # print(df['负责人'].values[0])
        #     project_names = df[names[0]].values
        #     type = df[names[2]].values[0]
        #     project_id = df[names[3]].values
        #     money = df[names[4]].values
        #     people = df[names[5]].values
        #     university = df[names[6]].values
        #     accpted = df[names[7]].values
        #     start = df[names[8]].values
        #     end = df[names[9]].values
        #     total = len(project_names)
        #     xiugai[id][type]['num']=total
        #     for i in range(0, total):
        #         id = people[i] + "_" + university[i]
        #         # if id not in author_info:
        #         # ids.append(id)
        #         # author_info[id] = {}
        #         # if type not in author_info[id]:
        #
        #         # print(type)
        #         # for t in types:
        #         # author_info[id][t] = {}
        #         # author_info[id][t]['num'] = 0
        #
        #         # xiugai[id][t]['info'] = []
        #
        #         # print(id)
        #         # author_info[id][type]['num']+=1
        #         info = {}
        #         info['title'] = project_names[i]
        #         info['project_id'] = project_id[i]
        #         info['money'] = money[i]
        #         info['accepted'] = accpted[i]
        #         info['start'] = start[i]
        #         info['end'] = end[i]
        #         xiugai[id][type]['info'].append(info)
        #     os.remove(file)
        with open('professors2.json', 'w', encoding='utf-8') as f:
            json.dump(xiugai, f, ensure_ascii=False)
    print(id,' is saved')
    print(num,'/',length)