# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 22:47
# @Author  : yhq
# @FileName: getDatas.py
# @Software: PyCharm
from bs4 import  BeautifulSoup
from urllib.request import *

import numpy as np

from random import randint
import re
import json
import requests
url_head = "http://apps.webofknowledge.com"

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

# form_data = {
#             'fieldCount': 1,
#             'action': 'search',
#             'product': 'UA',
#             'search_mode': 'GeneralSearch',
#             'SID': "5FqmyIGAVflLDapnkDy",
#             'max_field_count': 25,
#             'formUpdated': 'true',
#             'value(input1)': 'BioMed Research International',
#             'value(select1)': 'SO',
#             'value(hidInput1)': '',
#             'limitStatus': 'collapsed',
#             'ss_lemmatization': 'On',
#             'ss_spellchecking': 'Suggest',
#             'SinceLastVisit_UTC': '',
#             'SinceLastVisit_DATE': '',
#             'period': 'Year Range',
#             'range': 'CUSTOM',
#             'startYear': '2018',
#             'endYear': '2020',
#             'update_back2search_link_param': 'yes',
#             'ssStatus': 'display:none',
#             'ss_showsuggestions': 'ON',
#             'ss_query_language': 'auto',
#             'ss_numDefaultGeneralSearchFields': 1,
#             'rs_sort_by': 'PY.D;LD.D;SO.A;VL.D;PG.A;AU.A'
#         }
# # url_nums = np.load('error2.npy')
# session = requests.session()
# random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
# headers = {
#     'User-Agent': random_agent,
#     }
# r = session.post("http://apps.webofknowledge.com/UA_GeneralSearch.do",data=form_data,headers = headers)
# cookie = requests.utils.dict_from_cookiejar(r.cookies)
# print(r.text)

# print(urls[470])
error = []
for i in range(131,6567):
    # param = {
    #
    #     'product': 'UA',
    #     'search_mode': 'GeneralSearch',
    #     'SID': '5FqmyIGAVflLDapnkDy',
    #     'qid': '52',
    #     'page': '1',
    #     'doc': str(i),
    # }
    print('saving...')
    random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
    headers = {

        'User-Agent': random_agent,
        # 'Host': 'apps.webofknowledge.com',
        # 'Upgrade-Insecure-Requests' : '1'


    }
    data = {}
    # print(session.cookies)
    # headers1 = {
    #     'User-Agent': random_agent,
    #     'Host': 'apps.webofknowledge.com',
    #     'Upgrade-Insecure-Requests': '1',
    # }
    try:
        req =Request("http://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=5&SID=6D74rlIXulb6R81IgPl&page=1&doc="+str(i+1),headers=headers)

        # req.encoding = req.apparent_encoding
        # print(urls[0])
        html = urlopen(req,timeout=10).read().decode('utf-8')

        # if i == 0:
        #     print(html)

        soup = BeautifulSoup(html, features='lxml')
        # if i ==2236:
        #     print(soup)
        authors = soup.find_all(text=re.compile('(corresponding author)'))
        # print(authors)
        if len(authors)==0:
            continue
        data['author'] = authors[0].split('(')[0]
        adress = soup.find_all("td", {"class": "fr_address_row2"})

        data['adress'] = adress[0].get_text().split('.')[0]
        emails = soup.find_all("a", {"class": "snowplow-author-email-addresses"})

        for j in range(len(emails)):
            emails[j] = emails[j].get_text()
        data['emails'] = emails
        data['title']=soup.find("div",{"class":"title"}).get_text().replace("\n", "")

        with open('Molecular Medicine Reports/' + str(i) + '.json', 'w', encoding='utf-8') as f:
            # print(1)
            json.dump(data, f, ensure_ascii=False)
        print(str(i),'.json is saved.')
    except:
        print('error!')
        error.append(i)
    np.save('error4.npy',error)




