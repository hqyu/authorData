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
import time
from selenium import webdriver
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
#             'value(input1)': ' Journal of International Medical Research',
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
# url_nums = np.load('error2.npy')
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
qikan=[
'OncoTargets and Therapy',
'Cancer Cell International',
'Medical science monitor']
range1=[100,400,0]
range2=[3198,1219,3206]
for j in range(len(qikan)):
    for i in range(range1[j], range2[j]):
        if j==2 and i>130 and i<999:
            continue
        print(i,"j:",j,"range:",range1[j],",",range2[j],"qikan:",qikan[j])
        if i % 100 == 0:
            try:
                browser = webdriver.Chrome()
                browser.get(
                    "http://apps.webofknowledge.com/UA_GeneralSearch_input.do;jsessionid=9393A82BA1E11E2D71EA3E0FADF84AE4?product=UA&search_mode=GeneralSearch&SID=5DhuJubPl7k8LZ43PaB&preferencesSaved=")
                # browser.close()
                browser.get(
                    "http://apps.webofknowledge.com/UA_GeneralSearch_input.do;jsessionid=9393A82BA1E11E2D71EA3E0FADF84AE4?product=UA&search_mode=GeneralSearch&SID=5DhuJubPl7k8LZ43PaB&preferencesSaved=")
                time.sleep(5)
                input = browser.find_element_by_xpath(
                    '/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-search\']/div[@class=\'block-search-content\']/div[@class=\'search-criteria\']/div[@class=\'search-criteria-list\']/table[@id=\'search_table\']/tbody/tr[@id=\'searchrow1\']/td[@class=\'search-criteria-cell1\']/div[@id=\'container(input1)\']/input[@id=\'value(input1)\']')

                input.send_keys(qikan[j])
                # btn = browser.find_element_by_xpath('/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-search\']/div[@class=\'block-search-content\']/div[@class=\'search-criteria\']/div[@class=\'search-criteria-list\']/table[@id=\'search_table\']/tbody/tr[@id=\'searchrow1\']/td[@class=\'search-criteria-cell2\']/span[@class=\'select2 select2-container select2-container--medium\']/span[@class=\'selection\']/span[@class=\'select2-selection select2-selection--single\']/span[@id=\'select2-select1-container\']')
                # btn.click()
                # btn2 = browser.find_element_by_xpath('/html/body/span[@class=\'select2-container select2-container--medium select2-container--open\']/span[@class=\'select2-dropdown select2-dropdown--below\']/span[@class=\'select2-results\']/ul[@id=\'select2-select1-results\']/li[@id=\'select2-select1-result-c5wy-SO\']')
                # btn2.click()
                # btn3=browser.find_element_by_xpath('/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-settings\']/div[@id=\'timespan\']/div[@class=\'criteria-item\'][2]/div/span[@class=\'select2 select2-container select2-container--yeardropdown select2-container--below\']/span[@class=\'selection\']/span[@class=\'select2-selection select2-selection--single\']/span[@id=\'select2-range-b4-container\']')
                # btn3.click()
                # btn4=browser.find_element_by_xpath('/html/body/span[@class=\'select2-container select2-container--yeardropdown select2-container--open\']/span[@class=\'select2-dropdown select2-dropdown--below\']/span[@class=\'select2-results\']/ul[@id=\'select2-range-b4-results\']/li[@id=\'select2-range-b4-result-3eff-CUSTOM\']')
                # btn4.click()
                # btn5=browser.find_element_by_xpath('/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-settings\']/div[@id=\'timespan\']/div[@class=\'criteria-item\'][3]/div[@class=\'timespan_custom\']/span[@class=\'select2 select2-container select2-container--yeardropdown\'][1]/span[@class=\'selection\']/span[@class=\select2-selection select2-selection--single\']/span[@id=\'select2-startYear-rc-container\']')
                # btn5.click()
                # input2=browser.find_element_by_xpath('/html/body/span[@class=\'select2-container select2-container--yeardropdown select2-container--open\']/span[@class=\'select2-dropdown select2-dropdown--below\']/span[@class=\'select2-search select2-search--dropdown\']/input[@class=\'select2-search__field\']')
                # input.send_keys('2018')
                # btn6=browser.find_element_by_xpath('/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-settings\']/div[@id=\'timespan\']/div[@class=\'criteria-item\'][3]/div[@class=\'timespan_custom\']/span[@class=\'select2 select2-container select2-container--yeardropdown\']/span[@class=\'selection\']/span[@class=\'select2-selection select2-selection--single\']/span[@id=\'select2-endYear-wi-container\']')
                # btn6.click()
                # input3=browser.find_element_by_xpath('/html/body/span[@class=\'select2-container select2-container--yeardropdown select2-container--open\']/span[@class=\'select2-dropdown select2-dropdown--below\']/span[@class=\'select2-search select2-search--dropdown\']/input[@class=\'select2-search__field\']')
                # input3.send_keys('2020')
                button = browser.find_element_by_xpath(
                    '/html/body/form[@id=\'UA_GeneralSearch_input_form\']/div[@class=\'block-search\']/div[@class=\'block-search-content\']/div[@class=\'search-criteria\']/div[@class=\'search-criteria-list\']/table[@id=\'search_table\']/tbody/tr[@id=\'searchrow1\']/td[@class=\'search-criteria-cell3\']/span[@id=\'searchCell1\']/span[@class=\'searchButton\']/button[@class=\'large-button primary-button margin-left-10\']')
                button.click()
                time.sleep(5)

                # text = browser.page_source
                # print(browser.current_url)
                new_url = browser.current_url
                sid = re.findall(r'SID=\w+&', new_url)[0].replace('SID=', '').replace('&', '')
                browser.quit()
                # print(sid)
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

                form_data = {
                    'fieldCount': 1,
                    'action': 'search',
                    'product': 'UA',
                    'search_mode': 'GeneralSearch',
                    'SID': sid,
                    'max_field_count': 25,
                    'formUpdated': 'true',
                    'value(input1)': qikan[j],
                    'value(select1)': 'SO',
                    'value(hidInput1)': '',
                    'limitStatus': 'collapsed',
                    'ss_lemmatization': 'On',
                    'ss_spellchecking': 'Suggest',
                    'SinceLastVisit_UTC': '',
                    'SinceLastVisit_DATE': '',
                    'period': 'Year Range',
                    'range': 'CUSTOM',
                    'startYear': '2018',
                    'endYear': '2020',
                    'update_back2search_link_param': 'yes',
                    'ssStatus': 'display:none',
                    'ss_showsuggestions': 'ON',
                    'ss_query_language': 'auto',
                    'ss_numDefaultGeneralSearchFields': 1,
                    'rs_sort_by': 'PY.D;LD.D;SO.A;VL.D;PG.A;AU.A'
                }
                # url_nums = np.load('error2.npy')
                session = requests.session()
                random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
                headers = {
                    'User-Agent': random_agent,
                }
                r = session.post("http://apps.webofknowledge.com/UA_GeneralSearch.do", data=form_data, headers=headers)
                # print(r.url)
                headers = {
                    'User-Agent': random_agent,
                }
                req = Request(url=r.url, headers=headers)
                html = urlopen(req).read().decode('utf-8')
                soup = BeautifulSoup(html, features='lxml')
                datas = soup.find_all("a", {"class": "smallV110 snowplow-full-record"})
                # print(datas[0]['href'])
                current = datas[0]['href'][:-1]
            except:
                i=i-1
                continue
        # param = {
        #
        #     'product': 'UA',
        #     'search_mode': 'GeneralSearch',
        #     'SID': '5FqmyIGAVflLDapnkDy',
        #     'qid': '1',
        #     'page': '1',
        #     'doc': str(i),
        # }
        print('url:',url_head + current + str(i + 1))
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
            req = requests.get(url_head + current + str(i + 1), headers=headers, timeout=10)
            print("get successfully!")
            req.encoding = req.apparent_encoding
            # print(urls[0])
            # html = urlopen(req,timeout=10).read().decode('utf-8')

            # if i == 0:
            #     print(html)

            soup = BeautifulSoup(req.text, features='lxml')
            # if i ==2236:
            #     print(soup)
            authors = soup.find_all(text=re.compile('(corresponding author)'))
            # print(authors)
            if len(authors) == 0:
                continue
            data['author'] = authors[0].split('(')[0]
            adress = soup.find_all("td", {"class": "fr_address_row2"})

            data['adress'] = adress[0].get_text().split('.')[0]
            emails = soup.find_all("a", {"class": "snowplow-author-email-addresses"})

            for m in range(len(emails)):
                emails[m] = emails[m].get_text()
            data['emails'] = emails
            data['title'] = soup.find("div", {"class": "title"}).get_text().replace("\n", "")

            with open(qikan[j]+'/' + str(i) + '.json', 'w', encoding='utf-8') as f:
                # print(1)
                json.dump(data, f, ensure_ascii=False)
            print(str(i), '.json is saved.')
        except:
            print('error!')
            error.append(i)
        np.save('error3.npy', error)




