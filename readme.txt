1、安装chrome插件：Enhancer for YouTube™
2、在插件设置中，开启自定义脚本选项，并填入以下内容：
var url = window.location.href;
window.location.href="f1:"+url;
3、在config中配置，不用代理，可以不写 “” 这样，pwd_file中填入当前文件夹路径，例如默认示例，其他可以不管。
4、在F1.reg中相应位置填入路径，如默认所示（你能看懂的~）
5、运行F1.reg加入私有协议。
6、播放youtube视频时，点击Enhancer for YouTube™的自定义脚本按钮即可下载。
#####################
youtube-dl.exe可能会需要更新，下载最新放进去替换即可。
