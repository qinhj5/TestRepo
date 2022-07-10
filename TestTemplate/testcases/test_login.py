# -*- coding: utf-8 -*-
import os
from TestTemplate.common.unit import Unit, Util
from TestTemplate.pages.login_page import LoginPage


class TestLogin(Unit):

    # 获取testcases文件夹路径
    testcases_dir = os.path.dirname(os.path.abspath(__file__))

    def test_login_without_password(self):
        """
        测试无密码登录
        """
        lp = LoginPage(self.driver)
        # 读取数据文件第一行数据
        data = Util.get_data_by_row(os.path.join(self.testcases_dir, Util.get_config()['csvPath']), 1)
        lp.login_action(*data)

        self.assertTrue(lp.check_miss_pw_prompt())

    def test_login_without_username(self):
        """
        测试无账号登录
        """
        lp = LoginPage(self.driver)
        # 读取数据文件第二行数据
        data = Util.get_data_by_row(os.path.join(self.testcases_dir, Util.get_config()['csvPath']), 2)
        lp.login_action(*data)

        self.assertTrue(lp.check_miss_un_prompt())
