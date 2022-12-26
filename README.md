# 簡易機器人（計算理論期末project）
## 前言
因爲之前都沒有寫過linebot，甚至連python也是第一次接觸，所以我只做了一些簡單功能的機器人

## 功能

1.次方

第一個數字是任意數

第二個數字是正整數


之後就會給出答案

2.簡易計算機

先打出自己要算的數字

之後選擇要的功能

然後就會給出相對應的答案

3.fsm圖

會給出fsm的圖

## FSM圖
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/fsm.jpg)

state説明

user=初始狀態

power_input_num=次方功能下的任意數

power_input_num1=次方功能下的正整數

power_ans=次方的答案

cal_input_num2=計算機功能下的第一個數字

cal_input_num3=計算機功能下的第二個數字

cal_input_symbol=計算機功能下的運算符號

cal_ans=計算機的答案

## 操作示範
1.隨便輸入英文字母來開始linebot的操作
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/1.jpg)
2.之後就可以選擇要使用的功能 我們依序從第一個介紹 

按下或輸入計算次方，之後依照指示打出你要計算的數字
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/2.jpg)
3.按下返回主選單之後就可以選著其他的功能來操作
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/3.jpg)
4.這裏我們按下簡易計算機，跟著指示打出要計算的數字
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/4.jpg)
5.然後我們便可以選著我們要使用的加減乘除了

這裏我就示範乘法
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/5.jpg)
6.按下返回主選單就可以換其他操作
我們這裏就按下fsm圖來完成最後一個功能
![image](https://raw.githubusercontent.com/sl111000/linebot/master/img/6.jpg)





## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
