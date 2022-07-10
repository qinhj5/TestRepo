# -*- coding: utf-8 -*-
import os
import sys

# 获取main文件夹路径
main_dir = os.path.dirname(os.path.abspath(__file__))
# 将项目目录添加到环境变量
sys.path.append(os.path.join(main_dir, '../../'))

import unittest
from TestTemplate.common.HTMLTestRunner_cn import HTMLTestRunner
from TestTemplate.common.util import Util


if __name__ == '__main__':

    # 将符合条件的测试用例组装到测试套件
    discover = unittest.defaultTestLoader.discover(os.path.join(main_dir, '../testcases/'),
                                                   pattern=Util.get_config()['testPattern'])

    now = Util.get_format_time()

    # 使用HTMLTestRunner（中文版）生成测试报告
    runner = HTMLTestRunner(
        title=Util.get_config()['testTitle'],
        description=Util.get_config()['testVer'],
        stream=open(os.path.join(main_dir, '../reports/') + now + '-report.html', 'wb'),
        verbosity=2
    )

    runner.run(discover)
