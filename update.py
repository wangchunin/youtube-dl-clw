import requests
#下载地址
Download_addres='http://www.youtube-dl.org/downloads/latest/youtube-dl.exe'
#把下载地址发送给requests模块
f=requests.get(Download_addres)
#下载文件
with open("bin/youtube-dl.exe","wb") as code:
     code.write(f.content)