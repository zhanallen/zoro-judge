# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:58:52 2023

@author: allen

請讓使用者個別輸入當天的年份、月份及日期，
再以格式化方式輸出。
假設今天是2010年1月1日，
使用者分別輸入「2010」、「1」、「1」，
然後程式再輸出2010.01.01。

"""

x = input().replace("」", "").replace("「", "").split("、")    # 先把上下括號去掉，使用頓號進行切割
if (len(x[1]) < 2):    # 如果月跟日只有個位數就在前面加0
    x[1] = "0"+x[1]
if (len(x[2]) < 2):
    x[2] = "0"+x[2]
a = ".".join(x)    # 把x串列用.合併成一個字串
print(a)