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
import numpy as np
a = np.load('ids2.npy')
for i in a:
    print(i)
# # length=len(keywords)
# # for i in range(length):
# #     worksheet.write(0,i+3,keywords[i])
# lieming=['姓名',
# '单位',
# '类型',
# '项目名称',
# '项目编号',
# '金额',
# '批准年份',
# '执行起自',
# '执行截至',
# '个人主页']
# workbook = xlwt.Workbook(encoding='gbk')
# worksheet = workbook.add_sheet("data")
# types = ['优秀青年基金项目','重点项目','重大项目','面上项目']
# with open('professors.json', 'r', encoding='gbk')as f:
#    infos = json.load(f)
# for l in range(len(lieming)):
#
#     # keywords = ['文章',
#     #                 '作者', '地址', '邮箱']
#
#     worksheet.write(0, l, lieming[l])
#
# num = 1
# for id in infos:
#
#     for type in types:
#         if infos[id][type]['num'] != 0:
#             projects = infos[id][type]['info']
#
#             for i in range(len(projects)):
#
#                 worksheet.write(num, 0, id.split("_")[0])
#                 worksheet.write(num, 1, id.split("_")[1])
#                 worksheet.write(num, 2, type)
#                 worksheet.write(num, 3, projects[i]['title'])
#                 worksheet.write(num, 4, projects[i]['project_id'])
#                 worksheet.write(num, 5, projects[i]['money'])
#                 worksheet.write(num, 6, projects[i]['accepted'])
#                 worksheet.write(num, 7, projects[i]['start'])
#                 worksheet.write(num, 8, projects[i]['end'])
#                 worksheet.write(num, 9, infos[id]['home_page'])
#                 num += 1
#
# workbook.save("detail.xls")