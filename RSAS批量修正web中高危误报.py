#__author__ = 'techxsh'
#   encoding : gb2312
import http.client
import http.cookiejar
import urllib.request
import urllib.parse
import re
import time
configdata = open('config.ini', 'rU', encoding='utf-8').read()
#print(configdata)
configlists = re.findall("= (.*?)	", configdata)
#print(configlists)
print(
    '''
            ####################################################
            ####  RSAS批量修正web中高危误报~Author:Techxsh  ####
            ####################################################
    '''
)
print("本辅助主要用于批量修复中高危误报，低危无法修复。\n")
loginurl = configlists[0]+"/user/login"
urlvulinfo = configlists[0]+"/report/urlVulInfo/"
fixbatchurl = configlists[0]+"/report/fixBatchWebScanVul"
username = configlists[1]
password = configlists[2]
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
#proxy_handler = urllib.request.ProxyHandler({'https': 'http://127.0.0.1:8080'}) #此行及以下两行，为挂代理，方便使用burpsuit调试
#proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
#opener = urllib.request.build_opener( cookie_support, proxy_handler, proxy_auth_handler)
opener = urllib.request.build_opener(cookie_support)
urllib.request.install_opener(opener)
print("正在登录...")
logindata = opener.open(loginurl).read()
#print(logindata.decode("utf-8"))
csrf_token = re.search("name=\"csrf_token\" value=\"(.*?)\"", str(logindata)).group(1)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
           'Referer': configlists[0]+'/user/requireLogin'}
logindata = {'user[account]': username, 'user[password]': password, 'csrf_token': csrf_token}
logindata = urllib.parse.urlencode(logindata).encode("utf-8")
loginreq = urllib.request.Request(loginurl, logindata, headers)
loginres = opener.open(loginreq).read().decode("utf-8")
#print(loginres)
if '您好' in loginres:
    print("登录过程已完成")
else:
    print("登录过程未完成，请检查")
    exit()
idlists = []
fixids = input("输入需要修复任务的ID，用逗号隔开[格式：100,101-125,135,145-140]\n请输入：")
#fixids = "100,200,300,100-120"
fixlists = fixids.split(",")
print("即将修正的任务ID：%s" % fixlists)
for fixlist in fixlists:
    if "-" in fixlist:
        templist = fixlist.split("-")
        for templist in range(int(min(templist)), int(max(templist))+1):
            idlists.append(templist)
    else:
        idlists.append(fixlist)
#print(idlists)
keyword = input("输入需要修复漏洞的关键词：")
print("修正任务即将开始...")
for timer in range(0, 3):
    time.sleep(timer)
    print(3 - timer)
for idlist in idlists:
    fixurl = configlists[0]+"/report/urlVul/?id="+str(idlist)+"#"
    fixdata = opener.open(fixurl).read().decode("utf-8")
    #print(fixdata)
    vullists = re.findall("<tr class=\"_vul_title(.*?)</a></th>", fixdata)
    #print(vullists)
    for vuldata in vullists:
        if keyword in vuldata:
            vulid = re.search("vulId=\"(\d{1,10})\"><", vuldata).group(1)
            #print(vulid)
            vulurlpost = {"id": str(idlist), "dir": "/", "vid": vulid}
            vulurlpost = urllib.parse.urlencode(vulurlpost).encode("utf-8")
            vulurlreq = urllib.request.Request(urlvulinfo, vulurlpost)
            vulurldata = opener.open(vulurlreq).read().decode("utf-8")
            #print(vulurldata)
            vulurlids = re.findall("value='(\d{1,10})'", vulurldata)
            #print(vulurlids)
            infoIds = ""
            for vulurlid in vulurlids:
                infoIds += vulurlid + ','
            infoIds = infoIds[:-1]
            #print(infoIds)
            fixbatchpost = {"infoIds": infoIds, "_": ""}
            fixbatchpost = urllib.parse.urlencode(fixbatchpost).encode("utf-8")
            #print(fixbatchpost)
            fixbatchreq = urllib.request.Request(fixbatchurl, fixbatchpost)
            fixbatchdata = opener.open(fixbatchreq).read().decode("utf-8")
            if "成功" in fixbatchdata:
                print("%s号任务已修正" % idlist)
            else:
                print("%s号任务" % idlist+fixbatchdata)
        else:
            temp = 1
input("所有修正任务已完成。\n按Enter键退出...")