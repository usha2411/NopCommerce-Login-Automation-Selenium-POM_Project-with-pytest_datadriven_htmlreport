import time
from itertools import dropwhile
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker
from utilities import XLUtilitis

#config.ini
#read_properties
from utilities.read_properties import Read_Config
class Test_02_Admin_Login_data_driven:
    admin_page_url=Read_Config.get_admin_page_url()
    logger=Log_Maker.log_gen()
    path="D:/Pycharm/nopcommerce_automation/test_data/adim_login_data.xlsx"
    status_list=[]
    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("*****test_valid_admin_login_data_driven started*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp= Login_Admin_Page(self.driver)

        self.rows= XLUtilitis.getRowCount(self.path,'Sheet1')
        print("Number of rows",self.rows)

        for r in (2,self.rows+1):
            self.username=XLUtilitis.readData(self.path,'Sheet1',r,1)
            self.password = XLUtilitis.readData(self.path, 'Sheet1', r, 2)
            self.expected_login= XLUtilitis.readData(self.path, 'Sheet1', r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.expected_login=="Yes":
                    self.logger.info("test data passed")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.expected_login=="No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()
            elif act_title !=exp_title:
                if self.expected_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                elif self.expected_login == "No":
                    self.logger.info("test data passed")
                    self.status_list.append("Pass")
        print("status list is",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is passed")
            assert True





                    



