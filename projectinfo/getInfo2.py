from glob import glob
import pandas as pd
import json
# import xlrd
import numpy as np
files = sorted(glob('./xls3/*.xls'))
author_info = {}

# # print(files)
names = ['项目标题', '所属学部', '项目类型', '项目编号', '金额', '负责人', '单位', '批准年份', '执行起自', '执行截至']
types = ['优秀青年基金项目','重点项目','重大项目','国家杰出青年科学基金','面上项目','重大研究计划','联合基金项目']
ids=[]
# for file in files:
#
#     df = pd.read_excel(file, header=None, names=names)
#     df = df.drop(index=0)
#     df = df.drop(index=1)
#     # print(df['负责人'].values[0])
#     project_names = df[names[0]].values
#     type = df[names[2]].values[0]
#
#     project_id = df[names[3]].values
#     money = df[names[4]].values
#     people = df[names[5]].values
#     university = df[names[6]].values
#     accpted = df[names[7]].values
#     start =df[names[8]].values
#     end = df[names[9]].values
#     total = len(project_names)
#     for i in range(0,total):
#         id = people[i] + "_" + university[i]
#         if id not in author_info:
#             ids.append(id)
#             author_info[id] = {}
#             if type not in author_info[id]:
#                 if type not in types:
#                     author_info[id][type] = {}
#                     author_info[id][type]['num'] = 0
#                     author_info[id][type]['info']=[]
#                 #     continue
#                 # print(type)
#                 for t in types:
#                     author_info[id][t] = {}
#                     author_info[id][t]['num'] = 0
#
#                     author_info[id][t]['info'] = []
#
#         # print(id)
#         author_info[id][type]['num']+=1
#         info = {}
#         info['title'] = project_names[i]
#         info['project_id'] = project_id[i]
#         info['money'] = money[i]
#         info['accepted'] = accpted[i]
#         info['start'] = start[i]
#         info['end'] = end[i]
#         info['one']=''
#         info['two'] = ''
#         info['three'] = ''
#         author_info[id][type]['info'].append(info)
# print(author_info)
# np.save("ids2.npy",ids)
a = np.load('error2.npy')
with open('professors2.json', 'r', encoding='utf-8')as f:
    author_info = json.load(f)
# author_info = json.load('professor')
print('chucuo:')
print(a)
with open('home2.json', 'r', encoding='gbk')as f:
    home_pages = json.load(f)
    for page in home_pages:
        author_info[page]['home_page'] = home_pages[page]
with open( 'professors2.json', 'w', encoding='utf-8') as f:
    json.dump(author_info, f, ensure_ascii=False)
    print('json is saved')
