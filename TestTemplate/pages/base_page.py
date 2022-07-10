# -*- coding: utf-8 -*-
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        封装find_element
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        封装find_elements
        """
        return self.driver.find_elements(*loc)
