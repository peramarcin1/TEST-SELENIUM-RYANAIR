# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):


    def _verify_page(self):
        assert "Oficjalna strona Wizz Air" in self.driver.title
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@data-test="navigation-menu-signin"]')))

    def click_sign_in_btn(self):

        element = self.driver.find_element(*HomePageLocators.SIGN_IN_BTN)
        element.click()


