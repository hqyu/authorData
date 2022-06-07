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
qikan=['BioMed Research International',
'Molecular Medicine Reports',
'Computational and Mathematical Methods in Medicine',
'OncoTargets and Therapy',
'Cancer Cell International',
'Medical science monitor']

for l in range(len(qikan)):
    num = 1
    # keywords = ['文章',
    #                 '作者', '地址', '邮箱']
    workbook = xlwt.Workbook(encoding='gbk')
    worksheet = workbook.add_sheet("data")
    worksheet.write(0, 0, "title")
    worksheet.write(0, 1, "author")
    worksheet.write(0, 2, "address")
    worksheet.write(0, 3, "emails")
    total = sorted(glob(qikan[l]+'/*.json'))
    for file in total:
        with open(file, 'r', encoding='utf-8')as f:
            info = json.load(f)
            worksheet.write(num, 0, info['title'])
            worksheet.write(num, 1, info['author'])
            worksheet.write(num, 2, info['adress'])
            for j in range(len(info['emails'])):
                worksheet.write(num, j + 3, info['emails'][j])
            # for i in range(length):
            #     worksheet.write(num, i + 3,info['key_num'] [keywords[i]])
            num += 1

    workbook.save(qikan[l]+".xls")
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