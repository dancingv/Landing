# -*- coding: utf-8 -*
from pandas import Series,DataFrame
import pandas as pd
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# s = Series([100,'python','soochow','hello'])
# s1 = Series([100,'python','soochow','world'],index=['mark','title','university','hello'])
# data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
# s2 = DataFrame(data)
# #print(s2)
# print(dir())
# xingqi = '一二三四五六日'
# shuru = eval(input("请输入:"))
# print("今天是星期:"+xingqi[shuru-1])
# print(bin(0x10FFFF))
plt.plot([10,2,3,41,5,6,7,22])
plt.ylabel("Grade")
plt.xlabel("number")
plt.axis([-1,11,0,7])
plt.savefig('test',dpi=600)
plt.show()