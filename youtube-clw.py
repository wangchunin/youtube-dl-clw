#coding:utf-8
import os
import sys
import subprocess
import time
import msvcrt
import json
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw() # 不显示tk窗口


#函数部分
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))


def check_str(value):
    # 检查你输入的是否是字符类型
    if isinstance(value, str):
        '''
        # 判断字符串以什么结尾
        if value.endswith('***'):
            return 1
        '''
        # 判断字符串以什么开头
        if value.startswith('http'):
            return 1
        else:
            return 0
    else:
        return 0






def readInput(caption, default, timeout=3):
    start_time = time.time()
    sys.stdout.write('%s(%d秒自动重试,点击Enter立即重试):' % (caption,timeout))
    sys.stdout.flush()
    input = ''
    while True:
        ini=msvcrt.kbhit()
        try:
            if ini:
                chr = msvcrt.getche()
                if ord(chr) == 13:  # enter_key
                    break
                elif ord(chr) >= 32:
                    input += chr.decode()
        except Exception as e:
            pass
        if len(input) == 0 and time.time() - start_time > timeout:
            break
    print ('')  # needed to move to next line
    if len(input) > 0:
        return input+''
    else:
        return default
 
 

try:
    print("开始时间："+GetNowTime())
    url = sys.argv[1]
    new_url_without_f1 = url.replace('f1:','',1)
    new_url = new_url_without_f1
    pwd_file = os.path.split(sys.argv[0])[0].replace("/", "\\").replace("\\", "\\\\")
    while True:
        Folderpath = filedialog.askdirectory(title=u'选择文件夹')
        if len(Folderpath) != 0:
            break
        else:
            print("请选择下载位置！")
    Folderpath = Folderpath.replace(r"/", r"\\")
    print("下载路径：" + Folderpath)
    print("程序路径：" + pwd_file)

    with open(os.path.join(pwd_file, "config.json"),'r') as load_f:
      load_dict = json.load(load_f)
      print("json文件：")
      print(load_dict)
    #load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]


    dl_path = Folderpath
    proxy = load_dict['proxy']
    thread  = load_dict['thread']
    cache = load_dict['cache']





    if check_str(new_url):
        print ("下载网址："+new_url)
    else:
        print("error url")
        input("Prease <enter> to end!")
        sys.exit(1)




    path = os.getenv('PATH')

    os.environ['PATH']=path + ';' + pwd_file + "\\bin"
    print("当前PATH：" + os.getenv('PATH'))
    pwd = os.getcwd()
    print("初始环境路径：" + pwd)
    os.system("mkdir " + dl_path + "\\temp")

    os.chdir(dl_path)
    new_pwd = os.getcwd()


    print("osdir: " + new_pwd)




    cache_dir = dl_path + "\\temp"
    y= 'move {}  ' + dl_path
    x='--exec "{}"'.format(y)
    ar = "-x {}      -k {}M ".format(thread, cache)
    #print (x)
    #command='{}  &&  aria2c -h'.format(commandpath)
    #command = 'youtube-dl --proxy "https://127.0.0.1:1080"      --write-sub --no-playlist --audio-quality 0   {} "{}"'.format(x,new_url)

    #command = 'youtube-dl --proxy localhost:1081   -f bestvideo+bestaudio   --write-sub --no-playlist --audio-quality 0     {} "{}"'.format(x,new_url)
    #print(getText())
    if len(proxy)==0:
        command = 'youtube-dl --cache-dir={} --format=bestvideo+bestaudio  --merge-output-format mkv   --external-downloader aria2c --external-downloader-args "{}"    --write-sub --no-playlist  "{}"'.format(
            cache_dir, ar, new_url)
    else:
        command = 'youtube-dl --cache-dir={} --proxy {} --format=bestvideo+bestaudio  --merge-output-format mkv  --external-downloader aria2c --external-downloader-args "{}"    --write-sub --no-playlist   "{}"'.format(
            cache_dir, proxy, ar, new_url)
    #command = 'youtube-dl --proxy localhost:1081 -f bestvideo+bestaudio    --external-downloader aria2c --external-downloader-args "{}"    --write-sub --no-playlist --audio-quality 0  {} "{}"'.format(ar,x,new_url)
    #command = 'youtube-dl --proxy "https://127.0.0.1:1080" -f bestvideo+bestaudio --write-sub --audio-quality 0  --exec "move {} C:\" https://www.youtube.com/watch?v=9aOjGSC0R-Q&list=RDMM9aOjGSC0R-Q&start_radio=1'
    #print (command)
    #os.system(command)
    #output = os.popen(command)
    #char = output.read()


    returnCode=1

    while returnCode==1:

        returnCode = subprocess.call(command,shell=True)

        #print("returncode: ",returnCode)
        if returnCode:
            print("returncode: ",returnCode)
            #time1=time.time()
            choice = 0

            print('''下载链接出错，是否重试？
        1：重试
        2：退出''')
            '''
            while choice==1 || choice ==2 || (time.time()-time1)>3
                choice = input()
                time.sleep(0.1)
                '''
            choice=readInput('',1,6)
            choice = int(choice)
            #input(choice)
            if choice==2:
                returnCode = 0
                sys.exit(1)
                #print('returncodeEEEEEE:',returnCode)



        else:
            break

    #command="C:\\Users\\wangchunin\\Anaconda3\\Scripts\\youtube-dl --proxy localhost:1080   --write-sub  "+new_url
    #command="youtube-dl --proxy localhost:1080   --write-sub  "+new_url
    #os.system(command)

    print("结束时间："+GetNowTime())
    #print("共耗时：%d分钟",t)
    #print(char[-9:0])


    input("Prease <enter> to end!")
except Exception as e:
    print(e)
    input("程序出错：")

