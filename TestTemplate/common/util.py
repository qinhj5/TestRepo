# -*- coding: utf-8 -*-
import csv
import logging.config
import os
import sys
import time
import yaml


class Util:

    @classmethod
    def get_config(cls):
        """
        读取config文件夹下的配置文件并返回字典格式数据
        """
        with open(os.path.join(common_dir, '../config/config.yaml'), 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    @classmethod
    def get_format_time(cls):
        """
        返回格式化的时间点字符串
        """
        return time.strftime('%Y%m%d-%H%M%S')

    @classmethod
    def get_screenshot(cls, driver):
        """
        保存浏览器截图到screenshots文件夹下
        """
        logger.info('==========保存截图==========')
        now = Util.get_format_time()
        # 获取screenshots文件夹路径
        screenshots_dir = os.path.join(common_dir, '../screenshots/')
        driver.get_screenshot_as_file(screenshots_dir + now + '-screenshot.png')
        logger.info('截图保存为：' + now + '.png')

    @classmethod
    def get_csv_data(cls, csv_path):
        """
        读取csv文件中的测试用例数据
        """
        logger.info('==========读取数据==========')
        res = []
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader, 1):
                res.append(row)
            logger.info('==========读取完毕==========')
            return res


# 获取common文件夹路径
common_dir = os.path.dirname(os.path.abspath(__file__))
# 获取logs文件夹路径
logs_dir = os.path.join(common_dir, '../logs/')

# 创建名为__main__的Logger
logger = logging.getLogger(__name__)
# 设置日志输出等级
logger.setLevel(level=logging.INFO)
# 设置日志输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s line:%(lineno)d [%(levelname)s] %(message)s')


# 创建文件输出的Handler
fileHandler = logging.FileHandler(logs_dir + Util.get_format_time() + '-logging.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

# 创建控制台输出的Handler
streamHandler = logging.StreamHandler(sys.stdout)
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
