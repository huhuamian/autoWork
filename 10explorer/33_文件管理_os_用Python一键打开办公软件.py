# -*- coding: utf-8 -*-
# @Time : 2020/8/23 16:04
# @公众号 :Python自动化办公社区 
# @File : 33_文件管理_os_用Python一键打开办公软件.py
# @Software: PyCharm
# @Description:

import os


# teamViewer= 'C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe'
#os.popen(teamViewer)

chrome = 'D:\\software\\googleChrome\\chrome\\Google\\Chrome\\Application\\chrome.exe'
os.popen(chrome)
#
# wechat = 'D:\\software\\weChat\\WeChat.exe'
# os.popen(wechat)
#
# qqmusic = 'D:\\software\\qqmusic\\QQMusic.exe'
# os.popen(qqmusic)
#
# qqbrower = 'D:\\software\\qqbrowser\\QQBrowser\\QQBrowser.exe'
# os.popen(qqbrower)
#
#
# # snipaste = 'D:\\software\\snipaste\\install\\Snipaste-2.2.1-Beta2-x64\\Snipaste.exe'
# # os.popen(snipaste)
#
# # time.sleep(15)
#
# # egui = 'C:\\Program Files\\ESET\\ESET Endpoint Antivirus\\egui.exe'
# # os.popen(egui)
#
# # time.sleep(5)
#
# cloverpath = 'explorer D:\software\clover\install'
# os.popen(cloverpath)
#
# # time.sleep(15)
# clover = 'D:\\software\\clover\\install\\Clover v3.5.2 Build 19809\\Clover\\Clover.exe'
# os.popen(clover)
#
# # 打开任务管理器
taskmgr = 'taskmgr'
os.popen(taskmgr)
#
#
#
# print ('-'*20,'启动完成','-'*20)