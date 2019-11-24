import os
import sys

pwd = os.path.split(sys.argv[0])[0].replace("/", "\\").replace("\\", "\\\\")



print("当前路径：" + pwd)

try:
    with open(pwd + '\\F1.reg', 'r') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open(pwd + '\\F1.reg', 'w') as f:
        lines[-1] = r'@="\"{}\\youtube-clw.exe\" \"%1\""'.format(pwd)
        for line in lines:

            f.write('%s' % line)
        print("F1.reg修改成功！")
except:
    input("请右键管理员运行次程序！")


else:
    input("初始化完成，任意键退出！")