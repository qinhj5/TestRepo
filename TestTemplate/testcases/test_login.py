# -*- coding: utf-8 -*-
import os
from TestTemplate.common.unit import Unit, Util
from TestTemplate.pages.login_page import LoginPage
from TestTemplate.common.util import logger
from ddt import ddt, data


# 获取testcases文件夹路径
testcases_dir = os.path.dirname(os.path.abspath(__file__))


@ddt
class TestLogin(Unit):

    @data(*Util.get_csv_data(os.path.join(testcases_dir, Util.get_config()['csvPath'])))
    def test_login_fail(self, data):
        """
        测试登录失败
        """
        lp = LoginPage(self.driver)
        logger.info('读取数据：{}'.format(data))
        lp.login_action(*data)

        if data[1] == '':
            logger.info('==========断言无密码登录结果==========')
            self.assertTrue(lp.check_miss_pw_prompt())
        elif data[0] == '':
            logger.info('==========断言无密账号登录结果==========')
            self.assertTrue(lp.check_miss_un_prompt())
