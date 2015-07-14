#__author__ = 'techxsh'
# -*- coding: utf-8 -*-
#放至漏扫解压后的文件夹同目录
print(
    '''
            #################################################
            ####  RSAS主机漏扫关键词检索~Author:Techxsh  ####
            #################################################
    '''
)
print("放至漏扫解压后的文件夹同目录\n")
keyword = input("输入需要检索的漏扫关键词:")
import os
pwd = os.getcwd()
#print(pwd)
directorys = os.listdir()
#print(directorys)
for directory in directorys:
    try:
        files = os.listdir(directory)
        if "index.html" in str(files):
            a = open(pwd+"\\"+directory+"\\index.html", "r", encoding="utf-8")
            data = a.read()
            print(data)
            if keyword in data:
                print(directory)
            else:
                print("未找到")
    except os.error as e:
        temp = 1