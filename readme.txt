1、chrome、edge浏览器（支持Enhancer for YouTube™插件）
2、（1）不需要代理和已经购买了代理VPN并已经开启了系统层面代理（就是不需要翻和已经翻了的人）可以不管，直接看第三点。
   （2）对于有http代理端口的用户，请在config.json 中添加。格式："proxy": "http://127.0.0.1:1081",（删除字段即为不需要代理，但请保留格式:"proxy": "",）
3、右键管理员运行目录下Setup.exe
4、安装chrome插件：Enhancer for YouTube™
5、在插件设置中，开启自定义脚本选项，并填入EnhancerforYouTube.txt全部内容,如：
var url = window.location.href;
window.location.href="f1:"+url;
6、播放youtube视频时，点击Enhancer for YouTube™的自定义脚本按钮即可下载。
#####################
遇到程序出错运行目录下update.exe程序试试。
