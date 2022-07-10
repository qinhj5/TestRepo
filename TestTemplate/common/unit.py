# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from TestTemplate.common.util import logger, Util


class Unit(unittest.TestCase):

    def setUp(self):
        """
        测试用例执行前操作
        """
        logger.info('==========setUp==========')
        self.options = webdriver.ChromeOptions()
        # 关闭自动化控制提示，关闭日志输出
        self.options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(options=self.options)
        # 最大化浏览器窗口
        self.driver.maximize_window()
        # 设置隐式等待为5秒
        self.driver.implicitly_wait(5)
        # 打开配置文件中的测试地址
        self.driver.get(Util.get_config()['testUrl'])

    def tearDown(self):
        """
        测试用例执行后操作
        """
        logger.info('==========tearDown==========')
        # 退出浏览器，手动退出浏览器没有调用该语句会在后台驻留驱动进程
        self.driver.quit()
