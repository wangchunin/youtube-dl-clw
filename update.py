import requests
import json
import sys
import os
#下载地址
pwd = os.path.split(sys.argv[0])[0].replace("/", "\\").replace("\\", "\\\\")
with open(os.path.join(pwd,"config.json"),'r') as load_f:
  load_dict = json.load(load_f)



proxy = load_dict['proxy']
print("当前代理：" + proxy)
Download_addres='http://www.youtube-dl.org/downloads/latest/youtube-dl.exe'

proxies = {
  "http": "{}".format(proxy),
  "https": "{}".format(proxy),
}
#print(proxies)
#input()
#把下载地址发送给requests模块
print("正在下载，请耐心等待，如果config.json中配置了代理，会快一些！")
if len(proxy)==0:
    f = requests.get(Download_addres)
else:
    f=requests.get(Download_addres, proxies=proxies)

#下载文件
with open(os.path.join(pwd, "bin\\youtube-dl.exe"),"wb") as code:
     code.write(f.content)
print("完成，任意键退出！")
input()