#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: yhq
@contact:1318231697@qq.com
@version: 1.0.0
@file: json_to_excel.py
@time: 2021/9/15 15:58
"""
import json

import xlwt
from glob import glob

# length=len(keywords)
# for i in range(length):
#     worksheet.write(0,i+3,keywords[i])
lieming=['姓名',
'单位',
'优青',
'重点',
'重大',
'面上',
'杰青',
'重大研究计划','联合基金项目',
'F01','F02','F03','F04','F05','F06',
'C01','C02','C03','C04','C05','C06','C07','C08','C09','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21',
'H01','H02','H03','H04','H05','H06','H07','H08','H09','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24','H25','H26','H27','H28','H29','H30','H31',
'代表项目1','代表项目2',
'个人主页']
# types = ['优秀青年基金项目','重点项目','重大项目','国家杰出青年科学基金','面上项目']
workbook = xlwt.Workbook(encoding='gbk')
types = ['优秀青年基金项目','重点项目','重大项目','国家杰出青年科学基金','面上项目','重大研究计划','联合基金项目']
worksheet = workbook.add_sheet("data",cell_overwrite_ok=True)
with open('professors2.json', 'r', encoding='utf-8')as f:
   infos = json.load(f)
for l in range(len(lieming)):

    # keywords = ['文章',
    #                 '作者', '地址', '邮箱']

    worksheet.write(0, l, lieming[l])
    print(l)
    print(lieming[l])
    # worksheet.write(0, 1, "author")
    # worksheet.write(0, 2, "address")
    # worksheet.write(0, 3, "emails")

    # total = sorted(glob(qikan[l]+'/*.json'))
    # for file in total:
    #     with open(file, 'r', encoding='utf-8')as f:
    #         info = json.load(f)
    #         worksheet.write(num, 0, info['title'])
    #         worksheet.write(num, 1, info['author'])
    #         worksheet.write(num, 2, info['adress'])
    #         for j in range(len(info['emails'])):
    #             worksheet.write(num, j + 3, info['emails'][j])
    #         # for i in range(length):
    #         #     worksheet.write(num, i + 3,info['key_num'] [keywords[i]])
    #         num += 1
    #
    # workbook.save(qikan[l]+".xls")

# total = sorted(glob(qikan[3]+'/*.json'))
# for file in total:
#     with open(file, 'r', encoding='utf-8')as f:
#         info = json.load(f)
#         worksheet.write(num, 0, info['title'])
#         worksheet.write(num, 1, info['author'])
#         worksheet.write(num, 2, info['adress'])
#         for j in range(len(info['emails'])):
#             worksheet.write(num, j + 3, info['emails'][j])
#         # for i in range(length):
#         #     worksheet.write(num, i + 3,info['key_num'] [keywords[i]])
#         num += 1
# workbook.save(qikan[3]+".xls")

num = 1
for id in infos:
    # print( infos[id])
    pro1=''
    pro2=''
    money1=0
    money2=0
    if infos[id]['优秀青年基金项目']['num']==0 and  infos[id]['重点项目']['num']==0 and infos[id]['重大项目']['num']==0 and infos[id]['国家杰出青年科学基金']['num']==0 and (int)(infos[id]['面上项目']['num']) < 2:
        continue
    worksheet.write(num,0,id.split("_")[0])
    worksheet.write(num,1,id.split("_")[1])
    worksheet.write(num,2,infos[id]['优秀青年基金项目']['num'])
    worksheet.write(num, 3, infos[id]['重点项目']['num'])
    worksheet.write(num, 4, infos[id]['重大项目']['num'])
    worksheet.write(num, 5, infos[id]['面上项目']['num'])
    worksheet.write(num, 6, infos[id]['国家杰出青年科学基金']['num'])
    worksheet.write(num, 7, infos[id]['重大研究计划']['num'])
    worksheet.write(num, 8, infos[id]['联合基金项目']['num'])
    worksheet.write(num, 69, infos[id]['home_page'])
    for type in types:
        for info in infos[id][type]['info']:
            code = info['one']
            if len(code)!=0:
                if code[0] == 'F':
                    worksheet.write(num, 8+(int)(code[-3:-1]), 1)
                elif  code[0] == 'C':
                    worksheet.write(num, 14 + (int)(code[-3:-1]), 1)
                elif  code[0] == 'H':
                    worksheet.write(num, 35 + (int)(code[-3:-1]), 1)
            if 'money' not in info:
                continue
            if (int)((float)(info['money'])) > money1:
                money2 = money1
                pro2 = pro1
                pro1 = info['title']
                money1=(int)((float)(info['money']))
            elif (int)((float)(info['money'])) > money2:
                pro2 = info['title']
                money2 = (int)((float)(info['money']))

    worksheet.write(num, 67, pro1)
    worksheet.write(num, 68, pro2)
    num+=1
workbook.save("information2.xls")