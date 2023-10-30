# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:53:57 2023

@author: allen

根據輸入的兩個數字，輸出特定格式化的的數字。
第一個數字代表格式選擇，共有三種輸出格式。
第二個數字代表要輸出的數字。
例如，
輸入數字為1 5，則表示選擇格式一，並輸出[5.0000]，
輸入數字為2 5，則表示選擇格式二，並輸出[  5.00]，注意，前面有兩個空白。
輸入數字為3 5，則表示選擇格式三，並輸出[5.00  ]，注意，後面有兩個空白。

輸入說明
輸入兩個數字

輸出說明
輸出第二個數字的格式化型式

範例輸入 #1
1 5
範例輸出 #1
[5.0000]
範例輸入 #2
2 5
範例輸出 #2
[  5.00]
範例輸入 #3
3 5
範例輸出 #3
[5.00  ]

"""

x, y = map(float, input().split())
if(int(x) == 1):
    print("[%6.4f]" %y)
if(int(x) == 2):
    print("[%6.2f]" %y)
if(int(x) == 3):
    print("[%-6.2f]" %y)