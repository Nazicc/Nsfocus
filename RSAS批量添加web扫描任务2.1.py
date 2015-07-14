#__author__ = 'techxsh'
#在同目录的url.txt，一行一个写入需要扫描的url,格式:http://www.xxx.com。
# -*- coding : utf-8 -*-
import urllib
import urllib.request
import http.cookiejar
import linecache
import re
from urllib.parse import urlparse
i = 1 #起始url行数
configdata = open('config.ini', 'rU', encoding='utf-8').read()
#print(configdata)
configlists = re.findall("= (.*?)	", configdata)
#print(configlists)
print(
    '''
            ##################################################
            ####  RSAS批量添加web扫描任务~Author:Techxsh  ####
            ##################################################
    '''
)
print("在同目录的url.txt写入需批量待扫的url,格式:http://www.xxx.com\n")
taskname = input("输入任务名称：") #添加任务的名称
jtemp = len(open('url.txt', 'rU').readlines())
#print(jtemp)
if jtemp % 5 > 0:
    j = (int(jtemp/5) + 1)*5
else:
    j = jtemp
#print(j)
username = configlists[1]
password = configlists[2]
tasktype = configlists[3] #设置时间属性，timming为定时，directory为立即执行
year = configlists[4] #定时任务开始年
month = configlists[5]	#定时任务开始月
day = configlists[6] #定时任务开始日
moment = configlists[7] #定时任务开始时刻
count = 0
#登录的主页面
hosturl = configlists[0]+'/user/login'
posturl = configlists[0]+'/user/login'
addurl = configlists[0]+'/task/newAction/class/wavsm'
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
#proxy_handler = urllib.request.ProxyHandler({'https': 'http://127.0.0.1:8080'}) #此行及以下两行，为挂代理，方便使用burpsuit调试
#proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
#opener = urllib.request.build_opener( cookie_support, proxy_handler, proxy_auth_handler)
opener = urllib.request.build_opener(cookie_support)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(hosturl)
hdata = h.read()
csrf_token = re.search("name=\"csrf_token\" value=\"(.*?)\"", str(hdata)).group(1)
#print(csrf_token)
#print(hdata)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
           'Referer': configlists[0]+'/user/requireLogin'}
print("正在登录...")
postData = {
    'user[account]': username,
    'user[password]': password,
    'csrf_token': csrf_token
}
postData = urllib.parse.urlencode(postData).encode('utf-8')
request = urllib.request.Request(posturl, postData, headers)
#print(request)
response = urllib.request.urlopen(request)
text = response.read().decode('utf-8')
#print(text)
if '您好' in text:
    print("登录过程已完成")
else:
    print("登陆过程未完成,请检查配置。")
    exit()
for i in range(1, j, 5): #此处为一次添加的url数量，可自行修改
    task = [i, i+1, i+2, i+3, i+4]
    alldata = ''
    count+=1
    for url in task:
        data = linecache.getline('url.txt', url)
        alldata = data+ alldata
    addheader = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
                 'Referer' : configlists[0]+'/task/index/class/wavsm',
                 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarymFEYc464OOnWEQVn',
                 # 'Cookie': 'language=zh_CN; PHPSESSID=3cb94decfa4e66fe38cfe7a3bf0a65a7; report_tpl_id=0; selectedTasks='
    }
    adddata = '''

------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[task_type]"

webscan
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[targets_url]"

'''+alldata+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[name]"

'''+taskname+'~'+str(count)+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[type]"

'''+tasktype+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_year]"

'''+year+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_month]"

'''+month+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_day_moment]"

'''+day+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_time_moment]"

'''+moment+'''
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_time_day]"

00:00
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_week]"

1
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_time_week]"

00:00
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_day_month]"

1
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[cron_time_time_month]"

00:00
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[plugin_template_id]"

0
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_scan_method]"

1
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[webscan_username]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[webscan_usrpwd]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_proxy_type]"

HttpProxy
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_proxy_server]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_proxy_port]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_proxy_username]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_proxy_password]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[subdomains_scan]"

0
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[subdomains]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_scan_level]"

15
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_scan_type]"

width-first
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[scan_link_limit]"

-1
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_duplicate_page]"

no
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[dir_files_limit]"

50
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_case_sensitive]"

yes
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[udef_link]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[del_link]"


------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_filetype_to_check_backup]"

shtml,php,jsp,asp,aspx
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_backup_filetype]"

bak,old
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[webscan_timeout]"

30
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_plugin_threads]"

10
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_dir_level]"

1
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_dir_limit]"

3
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[ws_404]"

The\\\\ssystem\\\\scannot\\\\sfind\\\\sthe\\\\s(?:file|path)\\\\sspecified
page that no longer exists
the page you requested was not found
The page you requested cannot be found
The file you have requested is no longer available
The document you requested does not exist on this server
the page you\\\'re trying to reach is temporarily unavailable
the file you requested has moved or does not exist on our system
could not locate the page you requested
Document Not Found
Page Not Found
404 - File not found
404 - Object Not Found
404 Error
404 - Not Found
404 Not Found
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="newTask[report_format]"

html
------WebKitFormBoundarymFEYc464OOnWEQVn
Content-Disposition: form-data; name="start_ws"

å¼å§æ«æ
------WebKitFormBoundarymFEYc464OOnWEQVn--

'''
    adddata = adddata.encode('utf-8')
    req=urllib.request.Request(addurl, adddata, addheader)
    #proxy_handler = urllib.request.ProxyHandler({'https' : 'http://127.0.0.1:8080'})
    #proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    #opener = urllib.request.build_opener( cookie_support, proxy_handler, proxy_auth_handler)
    opener = urllib.request.build_opener(cookie_support)
    response = opener.open(req)
    page = response.read()
    print("第"+str(count)+"个任务添加成功")
print ("所有任务添加完毕，按Enter键退出...")
input()