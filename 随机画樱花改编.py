import turtle as t
import random
'''
版权声明：本文为依据CSDN博主「执笔写回憶」的原创文章作品改编而成，尝试改编了代码，如有兴趣可以查看正版原创。
原文链接：https://blog.csdn.net/z564359805/article/details/85861481
本文改编者author：alphaCai(from github)
'''
def trunk(Len):#整个是一个递归，函数中调用函数
    if Len > 3 :#递归结束的判定
        if 3 < Len < 8:#作为树枝末梢的处理
            t.pencolor(random.choice(['snow','lightcoral']))# 白 或 淡珊瑚色
            t.pensize(Len / 2)
        elif 8<= Len <=12:
            t.pencolor(random.choice(['snow','lightcoral','lightcoral']))#增加珊瑚色概率
            t.pensize(Len / 3)
        else:#一开始的树干处理
            t.pencolor('sienna')# 赭(zhě)色
            t.pensize(Len / 10)
        t.forward(Len)
        a,b=1.5 * random.random(),1.5 * random.random()
        t.right(20 * a)
        trunk(Len - 10 * b)#调用自身，增加下一枝节
        t.left(40 * a)        
        trunk(Len - 10 * b)#换了向左的角度后增加枝节
        t.right(20 * a)#转回原来角度，方便返回上一节点
        t.up()
        t.backward(Len)#画笔返回起始节点
        t.down()
        
def petal(m):#地上花瓣的处理
    t.pensize(3)
    t.pencolor('lightcoral')
    for i in range(m):#重复传送画笔至范围内随机位置画圆
        t.up()
        t.goto(random.randint(-200,200),random.randint(-150,-60))
        t.down()
        t.circle(1)

def tree():
    t.tracer(5,1)#这里用speed修改绘画速度也行
    t.hideturtle()#隐藏画笔
    t.screensize(bg='wheat')#麦色背景，默认大小
    t.pencolor('wheat')#和背景一致颜色，移动画笔不用提起
    t.left(90)
    t.goto(0,-100)#以初始位置为坐标中心点移动到x，y点
    trunk(60)#画樱花树
    petal(100)#点缀落下的花瓣
    t.exitonclick()#画完点击后可以退出
 
tree()
