# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from locators import RegisterPageLocators
import test_data.customer_data as td
import time



class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("geo.enabled", False)
        self.driver = webdriver.Firefox(profile)
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()
        time.sleep(2)

    def test_incorrect_email(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in_btn()
        time.sleep(2)

        login_page = LoginPage(self.driver)
        login_page.click_registration_btn()

        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_phone_number_country_code_field(td.valid_country)
        register_page.fill_phone_field(td.valid_phone)
        register_page.fill_email_field(td.invalid_email)
        register_page.fill_password_field(td.valid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.select_privacy_policy()
        register_page.click_register_btn()

        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices),1)
        self.assertEqual(visible_error_notices[0].get_attribute('innerText'),u"Nieprawidłowy adres e-mail")
        
        time.sleep(5)

    def test_incorrect_password(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in_btn()
        time.sleep(2)

        login_page = LoginPage(self.driver)
        login_page.click_registration_btn()

        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_phone_number_country_code_field(td.valid_country)
        register_page.fill_phone_field(td.valid_phone)
        register_page.fill_email_field(td.valid_email)
        register_page.fill_password_field(td.invalid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.select_privacy_policy()
        register_page.click_register_btn()

        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices),1)
        self.assertEqual(visible_error_notices[0].get_attribute('innerText'),u"Wpisz hasło")


        time.sleep(5)

    def test_incorrect_password(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in_btn()
        time.sleep(2)

        login_page = LoginPage(self.driver)
        login_page.click_registration_btn()

        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_phone_number_country_code_field(td.valid_country)
        register_page.fill_phone_field(td.valid_phone)
        register_page.fill_email_field(td.valid_email)
        register_page.fill_password_field(td.invalid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.select_privacy_policy()
        register_page.click_register_btn()

        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices),1)
        self.assertEqual(visible_error_notices[0].get_attribute('innerText'),u"Wpisz hasło")


        time.sleep(5)

    def test_incorrect_name(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in_btn()
        time.sleep(2)

        login_page = LoginPage(self.driver)
        login_page.click_registration_btn()

        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.invalid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_phone_number_country_code_field(td.valid_country)
        register_page.fill_phone_field(td.valid_phone)
        register_page.fill_email_field(td.valid_email)
        register_page.fill_password_field(td.valid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.select_privacy_policy()
        register_page.click_register_btn()

        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices),1)
        self.assertEqual(visible_error_notices[0].get_attribute('innerText'),u"Nieprawidłowy znak")


        time.sleep(5)

    def test_no_phone_number(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in_btn()
        time.sleep(2)

        login_page = LoginPage(self.driver)
        login_page.click_registration_btn()

        register_page = RegisterPage(self.driver)
        register_page.fill_name_field(td.valid_name)
        register_page.fill_surname_field(td.valid_surname)
        register_page.choose_gender(td.gender)
        register_page.fill_phone_number_country_code_field(td.valid_country)
        register_page.fill_phone_field(td.no_phone)
        register_page.fill_email_field(td.valid_email)
        register_page.fill_password_field(td.valid_password)
        register_page.fill_country_field(td.valid_country)
        register_page.select_privacy_policy()
        register_page.click_register_btn()

        error_notices = self.driver.find_elements(*RegisterPageLocators.ERROR_NOTICES)
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        self.assertEqual(len(visible_error_notices),1)
        self.assertEqual(visible_error_notices[0].get_attribute('innerText'),u"Please add a valid mobile phone number")


        time.sleep(5)




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
