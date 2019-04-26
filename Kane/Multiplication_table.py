# -*- encoding=utf-8 -*-
#打印九九乘法表
for a in range(1, 10):

    for b in range(1,a+1):
        #使用逗号取消自动换行
        print ("%s*%s=%s"%(a, b, a*b)),
    #使用\r\n实现大循环一次，换一行
    print ("\r\n")

