import json
import time
import urllib
from random import randint
from urllib.request import Request, urlopen

import aiohttp as aiohttp
import requests
import numpy as np
from bs4 import BeautifulSoup
import re
import ssl
import socket
ssl._create_default_https_context = ssl._create_unverified_context
def getHeader(headers, key):
    key_lower = key.lower()
    headers_lower = {k.lower(): v for k, v in headers.items()}
    if (key_lower in headers_lower):
        return headers_lower[key_lower]
    else:
        return ''
people= np.load('ids2.npy')
print(len(people))
name = people[0].split("_")[0]
univedrsity = people[0].split("_")[1]
home = {}
error = []
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
random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
cookie = 'HSID=AO3vGE3rMQXQfJaQh; SSID=Aa8H7CNI0TPBvbS1N; APISID=YvPqdAanZTeXZayc/AJqdYt46PoBvGoOfl; SAPISID=UFSHYeGb_1OfEkk4/A7obRBhyyI-aSoCpr; __Secure-1PAPISID=UFSHYeGb_1OfEkk4/A7obRBhyyI-aSoCpr; __Secure-3PAPISID=UFSHYeGb_1OfEkk4/A7obRBhyyI-aSoCpr; SID=KQgY2_zQ92sp50n9afXVlwzamqHbG4ggOOFIRpRfvatGA7Rqp1Sbznwoq52Pkf-nFPO7xw.; __Secure-1PSID=KQgY2_zQ92sp50n9afXVlwzamqHbG4ggOOFIRpRfvatGA7RqkFmBjKXQmnUvNv1-0SXADg.; __Secure-3PSID=KQgY2_zQ92sp50n9afXVlwzamqHbG4ggOOFIRpRfvatGA7Rq2Mjd4-1xwvg-YLbFkTY0_g.; SEARCH_SAMESITE=CgQIu5UB; NID=511=PEPHAUuh-vJOHnEFX0wSThVEwWC0wg-S3zacC8YQGUokbGfGJ20LdHdMZOXlHzw_U6cyjYsIcVpxNtdk5KZIAFvjJJ5cmtK8al5jFTB9qaB4cUeTaZ8Ty6iHRRRaH5a0h5MHqSyJiafedDakvBQmoXGM0okCzfoPLgLw5OyOc1XqkU7EnK7w0F59_sGWrpHXP4E4EejfSshGtKFocHXtXeUVNpG1MroZVpDzkroZ4C3zZrNSdryQ1SHcVkpAGvSTf6A5MYVAM1HMIUUd7RsDZBI45F_m0JCPWKXcqH9ntM-kZnuAWrWZr6pkrQ; 1P_JAR=2022-05-23-15; AEC=AakniGO_SSCXtnrWRmOzyWamEipVdFdEk6nYXsHEnzgfwCqD24lm3Lp4iBQ'
headers = {

    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    # 'User-Agent' : 'your bot 0.1',
    'Cookie':cookie

    # 'Content-Disposition':'attachment;filename=testjhh.xls'
    # 'Host': 'apps.webofknowledge.com',
    # 'Upgrade-Insecure-Requests' : '1'

}
str = '/url?q='
count = 0
for p in people:
    count+=1
    print(count)
    home[p] = ''
    name = p.split("_")[0]
    univedrsity = p.split("_")[1]
    url = "https://www.google.com.hk/search?q=" + urllib.parse.quote(name) + "+" + urllib.parse.quote(
        univedrsity) + "&newwindow=1&sxsrf=ALiCzsaOgQst930mMZ6PKIdoqJkwYhlGJg%3A1652950319218&ei=LwWGYsv8DIG0mAWv4oyAAQ&ved=0ahUKEwiL0O7kl-v3AhUBGqYKHS8xAxAQ4dUDCA4&oq=" + urllib.parse.quote(
        name) + "+" + urllib.parse.quote(
        univedrsity) + "&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABKBAhGGABQAFgAYABoAHAAeACAAQCIAQCSAQCYAQA&sclient=gws-wiz"
    try:

        req = Request(url, headers=headers)

        # req.encoding = req.apparent_encoding
        # print(urls[0])
        html = urlopen(req, timeout=10).read().decode('utf-8')
    except urllib.error.HTTPError as e:  # 响应错误
        try:
            print('啊哦')
            time.sleep(10)
            header = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
                # 'User-Agent' : 'your bot 0.1',
                'Cookie': cookie,
                'Retry-After': 3600
            }
            req = Request(url, headers=headers)

            # req.encoding = req.apparent_encoding
            # print(urls[0])
            html = urlopen(req, timeout=10).read().decode('utf-8')
        except:
            error.append(p)
            time.sleep(30)
            print('fuck')
            continue
    except urllib.error.URLError as e:
        print('fuck')
        error.append(p)
        continue
    #     retryAfter = "Retry-After"
    #     headers = e.headers
    #     sec = getHeader(headers, retryAfter)
    #     if len(sec) > 0:
    #         sec = int(sec)
    #         print( "请求过快，服务器要求待", sec, url)
    #         time.sleep(sec)  # If the rate limit is renewed in a minute, put 60 seconds, and so on.
    #     else:
    #         print("服务器拒绝了请求，表示请求过快。取消重试，请稍后再试！", url)
    #         break
    except:
        print('QITA')
        continue
    time.sleep(5)
    # if i == 0:
    #     print(html)
    # print(html)
    soup = BeautifulSoup(html, features='html.parser')
    # print(soup)
    divs = soup.find_all("div", attrs={'class': 'yuRUbf'})
    #
    for i in divs:
        s = i.find("a")
        s = s.get('href')
        print(s)
        if(len(s) > 1):
            flag = False
            for edu in s.split('.'):
                if edu == 'edu':
                    flag = True
                    home[p] = s
                    break
            if flag:

                break
    with open( 'home2.json', 'w', encoding='gbk') as f:
        json.dump(home, f, ensure_ascii=False)
        print('json is saved')

np.save('error2.npy',error)