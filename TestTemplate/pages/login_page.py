# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from TestTemplate.common.util import logger, Util
from TestTemplate.pages.base_page import BasePage


class LoginPage(BasePage):

    # 登录入口按钮
    login_entrance_btn = ('xpath', '//div[@id="u1"]//a[@name="tj_login"]')
    # 用户名输入框
    username_input = ('xpath', '//input[@name="userName"]')
    # 密码输入框
    password_input = ('xpath', '//input[@id="TANGRAM__PSP_11__password"]')
    # 登录按钮
    login_btn = ('xpath', '//input[@id="TANGRAM__PSP_11__submit"]')
    # 输入密码提示
    miss_pw_prompt = ('xpath', '//span[contains(text(),"请您输入密码")]')
    # 输入账号提示
    miss_un_prompt = ('xpath', '//span[contains(text(),"请您输入手机号/用户名/邮箱")]')

    def login_action(self, un, pw):
        """
        登录操作
        """
        logger.info('==========开始登录==========')

        logger.info('点击：登录入口')
        self.find_element(*self.login_entrance_btn).click()

        logger.info('输入账号：{}'.format(un))
        self.find_element(*self.username_input).send_keys(un)

        logger.info('输入密码：{}'.format(pw))
        self.find_element(*self.password_input).send_keys(pw)

        logger.info('点击：登录')
        self.find_element(*self.login_btn).click()

    def check_miss_pw_prompt(self):
        """
        检查是否找到输入密码提示并返回bool值
        """
        Util.get_screenshot(self.driver)

        try:
            self.find_element(*self.miss_pw_prompt)
        except NoSuchElementException:
            logger.error('未找到输入密码提示')
            return False
        else:
            logger.info('找到输入密码提示')
            return True

    def check_miss_un_prompt(self):
        """
        检查是否找到输入账号提示并返回bool值
        """
        Util.get_screenshot(self.driver)

        try:
            self.find_element(*self.miss_un_prompt)
        except NoSuchElementException:
            logger.error('未找到输入账号提示')
            return False
        else:
            logger.info('找到输入账号提示')
            return True
