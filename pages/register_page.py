# -*- coding: utf-8 -*-
import unittest
from base_page import BasePage
from locators import RegisterPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class RegisterPage(BasePage):
    def _verify_page(self):
        pass

    def fill_name_field(self, name):
        global name_field 
        name_field = self.driver.find_element(*RegisterPageLocators.NAME_FIELD)
        name_field.send_keys(name)

    def fill_surname_field(self, surname):
        global surname_field 
        surname_field = self.driver.find_element(*RegisterPageLocators.SURNAME_FIELD)
        surname_field.send_keys(surname)

    def choose_gender(self, gender):
        if (gender == 'male'):
            male_field = self.driver.find_element(*RegisterPageLocators.MALE_BTN)
            name_field.click()
            male_field.click()
        else:
            female_field = self.driver.find_element(*RegisterPageLocators.FEMALE_BTN)
            surename_field.click()
            female_field.click()

    def fill_phone_number_country_code_field(self, country):
        country_code = self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE_FIELD)
        country_code.click()
        country_code_input = self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE_INPUT_FIELD)
        country_code_input.send_keys(country)
        country_code_select = self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE_SELECT_FIELD)
        country_code_select.click()

    def fill_phone_field(self, phone):
        phone_field = self.driver.find_element(*RegisterPageLocators.PHONE_FIELD)
        phone_field.send_keys(phone)

    def fill_email_field(self, email):
        email_field = self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def fill_password_field(self, password):
        password_field = self.driver.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def fill_country_field(self, country):
        country_field = self.driver.find_element(*RegisterPageLocators.COUNTRY_FIELD)
        country_field.click()
        countries = self.driver.find_element(*RegisterPageLocators.COUNTRIES)
        countries_list = countries.find_elements_by_tag_name('label')
        for label in countries_list:
            country_to_choose = label.find_element_by_tag_name("strong")
            if country_to_choose.get_attribute("innerText") == country:
                country_to_choose.location_once_scrolled_into_view
                country_to_choose.click()
                break

    def select_privacy_policy(self):
        privacy_policy = self.driver.find_element(*RegisterPageLocators.PRIVACY_POLICY)
        privacy_policy.click()

    def click_register_btn(self):
        register_btn = self.driver.find_element(*RegisterPageLocators.REGISTER_BTN)
        register_btn.click()
