import os
import sys
import subprocess


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
    command = pwd + '\\F1.reg'
    returnCode = subprocess.call(command, shell=True)
    if returnCode==0:
        print("注册成功！")
    else:
        print("注册失败！")
        input("returnCode:"+returnCode)

except Exception as e:
    print(e)
    print("程序错误！")
    input("请右键管理员运行程序试试（如果你把程序放在C盘）！")


else:
    input("程序安装完成，任意键退出！")