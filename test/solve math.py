import cmath  # 复数运算库
import math  # 数学基本函数库

import matplotlib.pyplot as plt
import numpy as np
import sympy
from numpy import *  # 导入numpy的库函数

print(1/(2*math.pi*1000*10**(-4)))

# # 计算三角函数值
# arc=math.atan((6*3**0.5+8)/(8*3**0.5-6))
# print ("the arc={}".format(arc))
# print ("the arc={}*pi".format(arc/math.pi))
# print ('the arc= {}°'.format(math.degrees(arc)))

# x=np.arange(-10,10,0.01)
# y=0.03*np.cos(3*math.pi/2-math.pi*x/12)
# plt.plot(x,y)
# plt.legend('a')
# plt.show() 

# #以点画图
# U=(2.742,4.722,6.220,7.391,8.333,9.107,9.754,10.303,10.774)
# I=(27.421,23.612,20.732,18.478,16.666,15.178,13.934,12.878,11.971)
# plt.plot(U,I,'.')#描点
# #拟合
# z1=np.polyfit(U,I,1)#1阶拟合
# z2=np.polyfit(U,I,1)
# #多项式计算
# x=np.arange(0,14,0.1)
# y1=np.polyval(z1,U)
# y2=np.polyval(z2,U)
# #修饰
# plt.plot(U,I,label='original circuit')
# plt.plot(U,I,label='equivalent circuit')
# plt.xlabel("U/V")
# plt.ylabel("I/mA")
# plt.legend()
# plt.grid(True)#打开网格
# plt.show()

# #解方程
# x=sympy.symbols('x')
# y=sympy.solve(x+2*(x**2)-6,x)
# print(y)

# #矩阵运算
# a1=mat([[1,2],[3,4]])
# a2=mat([[3,4],[1,2]])
# a3=a1*a2
# print(a3)
# print (a3.T)
