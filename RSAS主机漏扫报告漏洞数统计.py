#__author__ = 'techxsh'
# -*- coding: utf-8 -*-
#放至漏扫解压后的文件夹同目录
import os
import re
print(
    '''
            #################################################
            ####  RSAS主机漏扫漏洞数统计~Author:Techxsh  ####
            #################################################
    '''
)
print("放至漏扫解压后的文件夹同目录，运行后结果在同目录out.txt\n")
input("按Enter键开始执行...")
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
            #print(data)
            if "<div id=\'ipList\' name=\"ipList\">" in data:
                hostdata = re.search("<div id='ipList' name=\"ipList\">(.*?)</div>", data, re.S).group(1)
                #print(hostdata)
                hostdata = re.sub("</td></tr>", "", hostdata)
                vaules = re.findall("<td>(\d{1,5})</td>", hostdata, re.S)
                print(vaules)
                high = 0
                middle = 0
                low = 0
                count = len(vaules)
                for i in range(0, count):
                    if i % 3 == 0:
                        high += int(vaules[i])
                    elif i % 3 == 1:
                        middle += int(vaules[i])
                    elif i % 3 == 2:
                        low += int(vaules[i])
                print(directory)
                name = re.search("--(.*?)_", directory).group(1)
                print(high, middle, low)
                out = open("out.txt", "a")
                out.writelines('%s    ' % name + '%s    ' % high + '%s    ' % middle + '%s    \n' % low)
                out.close()
            else:
                out = open("out.txt", "a")
                out.writelines(directory + "  error\n")
                out.close()
    except os.error as e:
        temp = 1
