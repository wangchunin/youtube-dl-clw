import os

pwd = os.getcwd()

pwd = pwd.replace("\\", "\\\\")
print("当前路径：" + pwd)
try:
    with open('EnhancerforYouTube.txt', 'r') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open('EnhancerforYouTube.txt', 'w') as f:
        lines[0] = 'var exec_path = "{}";\n'.format(pwd)
        for line in lines:

            f.write('%s' % line)
        print("EnhancerforYouTube.txt修改成功！")
except:
    print("请在程序目录下运行该程序！")


try:
    with open('F1.reg', 'r') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open('F1.reg', 'w') as f:
        lines[-1] = r'@="\"{}\\youtube-clw.exe\" \"%1\""'.format(pwd)
        for line in lines:

            f.write('%s' % line)
        print("F1.reg修改成功！")
except:
    print("请在程序目录下运行该程序！")

input("初始化完成，任意键退出！")