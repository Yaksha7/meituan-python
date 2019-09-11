# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://proxy1.countnet.cn:20807/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("13600000002")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("p").click()
        driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
        driver.find_element_by_link_text(u"普通新添").click()
        driver.find_element_by_css_selector("div.modal-content > div.modal-footer > label > button.btn.btn-primary").click()
        driver.find_element_by_id("btn_Save").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath("(//button[@type='button'])[91]").click()
        driver.find_element_by_link_text(u"到 待报价").click()
        driver.find_element_by_css_selector("#ConfirmModal1 > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-primary").click()
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertEqual(u"01A", driver.find_element_by_id("Status").get_attribute("value"))
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
