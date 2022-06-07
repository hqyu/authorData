import numpy as np
import json
ids = np.load('ids.npy')
types = ['优秀青年基金项目','重点项目','重大项目','国家杰出青年科学基金','面上项目']
length = len(ids)
with open('professors.json', 'r', encoding='utf-8')as f:
    xiugai = json.load(f)
num = 0
for id in ids:
    num+=1
    name = id.split("_")[0]
    university = id.split("_")[1]
    # xiugai[id]['面上项目']={}
    for t in types:
        # lefturl = "&age=&name=&person="+urllib.parse.quote(name)+"&no=&company="+urllib.parse.quote(university)+"&addcomment_s1=&addcomment_s2=&addcomment_s3=&addcomment_s4=&money1=&money2=&startTime=1997&endTime=2020&province_main=&subcategory=" + \
        #           urllib.parse.quote(t) + "&searchsubmit=true"
        # req = Request(postUrl + lefturl, headers=headers)
        #
        # # req.encoding = req.apparent_encoding
        # # print(urls[0])
        # try:
        #
        #     html = urlopen(req, timeout=10).read().decode('utf-8')
        # except:
        #     time.sleep(10)
        #     print('error')
        #     print(num,'/',length)
        # time.sleep(5)
        # soup = BeautifulSoup(html, features='html.parser')
        # # print(soup)
        # b = soup.find("b")
        # if b == None:
        #     xiugai[id][t]['num'] = 0
        #     print(num, '/', length)
        #     continue
        if t == '面上项目':
            if 'num' not in  xiugai[id][t]:
                xiugai[id][t]['num'] = 0
            if 'info' not in  xiugai[id][t]:
                xiugai[id][t]['info'] = []
        xiugai[id][t]['num']=len(xiugai[id][t]['info'])
        # tr = soup.find_all("tr")
        # university = ''
        # info = {}
        # infos=[]
        # for i in tr:
        #     td = i.find_all("td")
        #     if len(td) == 0:
        #         continue
        #     # info = {}
        #     if td[0].get_text() == name:
        #         info = {}
        #         info['project_id']=td[3].get_text()
        #         info['money']=td[2].get_text()
        #         info['accepted']=td[6].get_text()
        #     if td[0].get_text() == '题目':
        #         info['title'] = td[1].get_text()
        #     if td[0].get_text() == '执行时间':
        #         s=td[1].get_text().split("至")
        #         if len(s) == 0:
        #             info['start'] = 'false'
        #             info['end'] = 'false'
        #         if len(s) == 2:
        #             info['start'] = s[0]
        #             info['end'] = s[1]
        #             infos.append(info)
        #     if td[0].get_text() == '学科代码':
        #         b = re.findall('一级：(.*)二级：', td[1].get_text())
        #         if len(b) == 0:
        #             info['one'] = ''
        #         else:
        #             info['one'] = b[0]
        #         b = re.findall('二级：(.*)三级：', td[1].get_text())
        #         if len(b) == 0:
        #             info['two'] = ''
        #         else:
        #             info['two'] = b[0]
        #         b = td[1].get_text().split(":")
        #         if b[-1][-2:] == '三级':
        #             info['three'] = ''
        #         else:
        #             print(b[-1][-2:])
        #             info['three'] = b[-1]
        #
        # xiugai[id]['面上项目']["info"]=infos
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
        with open('professors.json', 'w', encoding='utf-8') as f:
            json.dump(xiugai, f, ensure_ascii=False)
    print(id,' is saved')
    print(num,'/',length)