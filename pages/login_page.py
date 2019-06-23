# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def _verify_page(self):
        pass

    def click_registration_btn(self):
        element = self.driver.find_element(*LoginPageLocators.REGISTRATION_BTN)
        element.click()
        
