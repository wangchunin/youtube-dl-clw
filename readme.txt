1、右键管理员运行目录下init.exe
2、运行F1.reg加入私有协议
3、安装chrome插件：Enhancer for YouTube™
4、在插件设置中，开启自定义脚本选项，并填入EnhancerforYouTube.txt全部内容,如：
var url = window.location.href;
window.location.href="f1:"+url;
3、在config中配置，不用代理，可以不写 "" 这样，例如默认示例，其他可以不管。
6、播放youtube视频时，点击Enhancer for YouTube™的自定义脚本按钮即可下载。
#####################
youtube-dl.exe可能会需要更新，下载最新放进去替换即可,也可以直接管理员运行（如果是C盘）update.exe程序更新youtube-dl.exe
http://www.youtube-dl.org/downloads/latest/youtube-dl.exe
每次下载为最新版本
