# -*- coding: utf-8 -*-
# @Time : 2020/8/23 2:26
# @公众号 :Python自动化办公社区 
# @File : 32_文件管理_os_用Python搜索文件.py
# @Software: PyCharm
# @Description:

# 搜索文件的程序
import os
list_all = []
# win/mac/linux
for root,dirs,files in os.walk('D:/software'):
    for name in files:
        file_path = os.path.join(root,name)
        if 'python' in name:
            print(os.path.split(file_path))

