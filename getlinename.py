# -*- coding: utf-8 -*-
# Python3.5
import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os

headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
all_url = 'https://zhengzhou.8684.cn'  ##开始的URL地址
start_html = requests.get(all_url, headers=headers)
#print (start_html.text)
Soup = BeautifulSoup(start_html.text, 'lxml')
class_name = ['bus_kt_r1','bus_kt_r2']
Network_list = []
for name in class_name:
    all_a = Soup.find('div',class_= name).find_all('a')
    for a in all_a:
        href = a['href'] #取出a标签的href 属性
        html = all_url + href
        second_html = requests.get(html,headers=headers)
        #print (second_html.text)
        Soup2 = BeautifulSoup(second_html.text, 'lxml')
        all_a2 = Soup2.find('div',class_='cc_content').find_all('div')[-1].find_all('a') # 既有id又有class的div不知道为啥取不出来，只好迂回取了
        for a2 in all_a2:
            information = []
            Network_list.append(a2.text)
# 定义保存函数，将运算结果保存为txt文件
def text_save(content,filename):
    # Try to save a list variable in txt file.
    file = open(filename,'w','utf-8')
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

# 输出处理后的数据
text_save(Network_list,'Network_bus.csv');