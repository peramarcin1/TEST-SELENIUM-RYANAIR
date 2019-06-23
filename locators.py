# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class HomePageLocators(object):
    SIGN_IN_BTN = (By.XPATH, '//button[@data-test="navigation-menu-signin"]')

class LoginPageLocators(object):
    REGISTRATION_BTN = (By.XPATH, "//button[text()='Rejestracja']")

class RegisterPageLocators(object):
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Imię']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='Nazwisko']")
    MALE_BTN = (By.XPATH, "//label[@for='register-gender-male']")
    FEMALE_BTN = (By.XPATH, "//label[@for='register-gender-female']")
    COUNTRY_CODE_FIELD = (By.XPATH, "//div[@class='phone-number__calling-code-selector__empty']")
    COUNTRY_CODE_INPUT_FIELD = (By.XPATH, "//input[@name='phone-number-country-code']")
    COUNTRY_CODE_SELECT_FIELD = (By.XPATH,'//*[@id="regmodal-scroll-hook-3"]/div[1]/div/div[1]/ul/li[2]' )
    PHONE_FIELD = (By.XPATH, "//input[@name='phoneNumberValidDigits']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-test='booking-register-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test='booking-register-password']")
    COUNTRY_FIELD = (By.XPATH, "//input[@data-test='booking-register-country']")
    COUNTRIES = (By.XPATH, "//div[@class='register-form__country-container__locations']")
    PRIVACY_POLICY = (By.XPATH, "//label[@for='registration-privacy-policy-checkbox'][@class='rf-checkbox__label']")
    REGISTER_BTN = (By.XPATH, "//button[@data-test='booking-register-submit']")
    ERROR_NOTICES = (By.XPATH, '//span[@class="rf-input__error__message"]/span')