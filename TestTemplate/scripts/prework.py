# -*- coding: utf-8 -*-
import os
import shutil

# 获取scripts文件夹路径
scripts_dir = os.path.dirname(os.path.abspath(__file__))
# 获取temp文件夹路径
temp_dir = os.path.join(scripts_dir, '../temp/')
# 获取reports文件夹路径
reports_dir = os.path.join(scripts_dir, '../reports/')
# 获取screenshots文件夹路径
screenshots_dir = os.path.join(scripts_dir, '../screenshots/')
# 获取logs文件夹路径
logs_dir = os.path.join(scripts_dir, '../logs/')


def move_files(src, des, postfix):
    """
    移动指定目录下指定后缀的文件到临时文件夹
    """
    for filename in os.listdir(src):
        if '.' + postfix in filename:
            shutil.move(src + filename, des)


if __name__ == '__main__':

    # 创建temp文件夹
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 将以往的报告/截图/日志移动至temp文件夹
    move_files(reports_dir, temp_dir, 'html')
    move_files(screenshots_dir, temp_dir, 'png')
    move_files(logs_dir, temp_dir, 'log')
