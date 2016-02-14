##############################################################################
#
# This is created for testing purposes.
# Testing Order functionality using Selenium.
#
##############################################################################
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCaseOrderPyhton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://automationpractice.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # Order by changing quantity, remove, continue shopping then proceed with check out
    def test_case_order_pyhton(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//ul[@id='homefeatured']/li[2]/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
        driver.find_element_by_xpath("//ul[@id='homefeatured']/li[3]/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
        driver.find_element_by_xpath("//ul[@id='homefeatured']/li[6]/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
        driver.find_element_by_css_selector("span.ajax_cart_product_txt_s.unvisible").click()
        driver.find_element_by_css_selector("i.icon-plus").click()
        driver.find_element_by_css_selector("#cart_quantity_up_6_31_0_0 > span").click()
        driver.find_element_by_css_selector("#cart_quantity_down_6_31_0_0 > span").click()
        driver.find_element_by_css_selector("#3_13_0_0 > i.icon-trash").click()
        driver.find_element_by_link_text("Continue shopping").click()
        driver.find_element_by_xpath("//ul[@id='homefeatured']/li[7]/div/div[2]/div[2]/a/span").click()
        driver.find_element_by_css_selector("div.layer_cart_overlay").click()
        driver.find_element_by_css_selector("#button_order_cart > span").click()
        driver.find_element_by_css_selector("#cart_quantity_up_7_34_0_0 > span").click()
        driver.find_element_by_css_selector("#cart_quantity_up_7_34_0_0 > span > i.icon-plus").click()
        driver.find_element_by_xpath("//div[@id='center_column']/p[2]/a/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
