# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:45:47 2023

@author: allen

給定一個正整數數字，輸出該數字高度的直角三角形。
例如，輸入5，則輸出

*

**

***

****

*****

以此類推。

輸入說明
輸入一正整數

輸出說明
輸出該正整數高度的直角三角形

範例輸入 #1
1
範例輸出 #1
*

"""

x = int(input())
for i in range(x):
    print("*" * (i+1))