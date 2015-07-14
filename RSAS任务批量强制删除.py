#__author__ = 'techxsh'
#   encoding : gb2312
#可批量删除在执行的任务。
import http.client
import http.cookiejar
import urllib.request
import urllib.parse
import re
import socket
loginurl = "https://10.238.72.55/user/login"
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
           'Referer': 'https://10.238.72.55/user/requireLogin'}
logindata = {'user[account]': 'admin', 'user[password]': 'nsfocus123', 'csrf_token': csrf_token}
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
delids = input("输入需要删除任务的ID，用逗号隔开[格式：100,101-125,135,145-140]\n请输入：")
#fixids = "100,200,300,100-120"
dellists = delids.split(",")
print("即将删除的任务ID：%s" % dellists)
for dellist in dellists:
    if "-" in dellist:
        templist = dellist.split("-")
        for templist in range(int(min(templist)), int(max(templist))+1):
            idlists.append(templist)
    else:
        idlists.append(dellist)
#print(idlists)
ids = re.sub(r"\[| |\]", "", str(idlists))
#print(ids)
delurl = "https://10.238.72.55/list/index/offset/0/count/25/op/delete/ids/"+ids+"/type/"
print("正在删除...")
try:	
    opener.open(delurl)
    print("指定任务已删除,按Enter键退出...")
    input()
except http.client.error as e:
    print(e)
except socket.error as e:
    print(e)