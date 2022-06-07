import ast
import os
from datetime import datetime

import xlwt
from bs4 import  BeautifulSoup
from urllib.request import *

import numpy as np

from random import randint
import re
import json
import requests
import time
# from selenium import webdriver
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
postUrl = "http://spencer.renlab.org/api/browse/listResult"
postUrl2 = " http://spencer.renlab.org/api/transcript/sequence"
os.environ['NO_PROXY'] = 'spencer.renlab.org'
# cancer = ["Anal canal cancer","Bile duct cancer","Bladder cancer","Breast cancer","Colon cancer","Gastric cancer","Kidney cancer","Leukemia","Liver cancer",
#           "Lung cancer","Ovary cancer","Prostate cancer","Skin cancer","Thyroid cancer","Tongue cancer"]
# tissue = [["Anal canal"],["Bile duct"],["Urinary bladder","Extracellualr vesicles"],["Breast","Breast epithelium","Blood serum microvesicles","Blood serum extracellular vesicles","Extracellular vesicles","Blood serum microvesicles phosphoproteomic","Saliva","Blood serum exosomes","Metastatic lymph nodes","Blood serum exosomes phosphoproteomic"],
#           ["Colon","Colon epithelium","Blood serum","Extracellular vesicles","Liver"],["Ascites","Blood serum exosomes","Myofibroblast"],["Kidney","Kidney epithelium","Blood plasma extracellular vesicles","Blood plasma extracellular vesicles phosphoproteomic"],
#           ["Blood plasma exosomes","Blood"],["Liver"],["Lung","Lung epithelium","Extracellular vesicles"],["Ovary","Blood plasma","Blood serum","Saliva"],
#           ["Prostate","Seminal plasma","Fibroblast","Kidney","Urinary extracellular vesicles"],["Skin"],["Urine","Blood serum"],["Fibroblasts exosomes"]]
# total = [[641],[603],[1671,413],[1073,322,274,268,716,268,71,268,534,268],[3533,1879,103,1207,2148],[692,260,416],[508,1018,92,92],[40,644],[362],
#          [2558,1216,357],[56,241,44,74],[358,234,592,245,280],[1578],[293,285],[731]]
cancer = ["Kidney cancer","Leukemia","Liver cancer",
          "Lung cancer","Ovary cancer","Prostate cancer","Skin cancer","Thyroid cancer","Tongue cancer"]
tissue = [["Kidney","Kidney epithelium","Blood plasma extracellular vesicles","Blood plasma extracellular vesicles phosphoproteomic"],
          ["Blood plasma exosomes","Blood"],["Liver"],["Lung","Lung epithelium","Extracellular vesicles"],["Ovary","Blood plasma","Blood serum","Saliva"],
          ["Prostate","Seminal plasma","Fibroblast","Kidney","Urinary extracellular vesicles"],["Skin"],["Urine","Blood serum"],["Fibroblasts exosomes"]]
total = [[508,1018,92,92],[40,644],[362],
         [2558,1216,357],[56,241,44,74],[358,234,592,245,280],[1578],[293,285],[731]]
error = []
count = 0
for x in range(len(cancer)):

    for y in range(len(tissue[x])):
        try:
            datas = []
            l = (int)(total[x][y] / 100)
            if(total[x][y] % 100 != 0):
                l+=1
            for z in range(0,l):


                random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
                a = z + 1;
                # pageNum = ""+ a
                print("cancer:" + cancer[x], "tissue:" + tissue[x][y], "page:" + (str)(a) + "/" + (str)(l))
                payloadData = {"cancer": cancer[x],
                               "tissue": tissue[x][y],
                               "studyList": ["All"],
                               "immunogenicity": None,
                               "validation": None,
                               "expression": None,
                               "simultaneous": None,
                               "pageSize": 100,
                               "total": total[x][y],
                               "pageNum": a,
                               "hasCountTotal": False}
                # 请求头设置
                payloadHeader = {
                    'Host': 'spencer.renlab.org',
                    'Content-Type': 'application/json',
                    'User-Agent': random_agent
                }
                # 下载超时
                timeOut = 25
                # 代理
                # proxy = "183.12.50.118:8080"
                # proxies = {
                #     "http": proxy,
                #     "https": proxy,
                # }

                r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
                dumpJsonData = json.dumps(payloadData)
                # print(f"dumpJsonData = {dumpJsonData}")
                res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut,
                                    allow_redirects=True)
                # 下面这种直接填充json参数的方式也OK
                # res = requests.post(postUrl, json=payloadData, headers=header)
                # print(f"responseTime = {datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
                text = res.text.replace('null', '0')
                text = text.replace('false', 'False')
                text = text.replace('true', 'True')
                # print(eval(text)["data"]["result"])
                info = eval(text)["data"]["result"]
                # print(info[0]["peptideId"])
                for i in info:
                    # print(type(i["relatedTranscriptId"]))
                    for j in i["relatedTranscriptId"].split(","):
                        print(j)
                        temp = i
                        payloadData2 = {"transcriptId": j}
                        r2 = requests.post(postUrl2, data=json.dumps(payloadData2), headers=payloadHeader)
                        dumpJsonData2 = json.dumps(payloadData2)
                        # print(f"dumpJsonData = {dumpJsonData}")
                        res2 = requests.post(postUrl2, data=dumpJsonData2, headers=payloadHeader, timeout=timeOut,
                                             allow_redirects=True)
                        text2 = res2.text.replace('null', '0')
                        text2 = text2.replace('false', 'False')
                        text2 = text2.replace('true', 'True')
                        # print(eval(text)["data"]["result"])
                        seq = eval(text2)["data"]
                        # print(j, seq)
                        temp["sequence"] = seq
                        # i["sequence"] = seq
                        # print(temp)
                        datas.append(temp)
            keys = list(datas[0].keys())
            workbook = xlwt.Workbook()
            worksheet = workbook.add_sheet("data")
            for xls in range(len(keys)):
                worksheet.write(0, xls, keys[xls])
            for data_info in range(len(datas)):
                for xls in range(len(keys)):
                    if len((str)(datas[data_info][keys[xls]])) > 32767:
                        continue
                    worksheet.write(data_info + 1, xls, datas[data_info][keys[xls]])

            workbook.save(cancer[x] + "_" + tissue[x][y] + ".xls")
            print(cancer[x] + "_" + tissue[x][y] + ".xls" + " is saved!")
        except:
            count+=1
            error.append(("cancer:" + cancer[x], "tissue:" + tissue[x][y]))
np.save("error_info.npy",error)
print("task finish! error data:"+count)
