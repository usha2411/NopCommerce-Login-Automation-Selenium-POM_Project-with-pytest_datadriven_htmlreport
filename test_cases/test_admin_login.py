from itertools import dropwhile
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from base_pages.login_admin_page import Login_Admin_Page
from utilities.custom_logger import Log_Maker

#config.ini
#read_properties
from utilities.read_properties import Read_Config
class Test_01_Admin_Login:
    admin_page_url=Read_Config.get_admin_page_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    invalid_username=Read_Config.get_invalid_username()
    logger=Log_Maker.log_gen()


# class Test_01_Admin_Login:
#     admin_page_url='https://admin-demo.nopcommerce.com/login'
#     username="admin@yourstore.com"
#     password="admin"
#     invalid_username="admin1234334.com"
    @pytest.mark.regression
    def test_title_verify(self,setup):
        self.logger.info("*****Test_01_Admin_Login*****")
        self.logger.info("*****Verification of admin login page title*****")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        actual_title=self.driver.title
        exp_title="nopCommerce demo store. Login"
        if actual_title==exp_title:
            self.logger.info("*****title verified*****")
            assert True
            self.driver.close()
        else:
            self.logger.info("*****Title not verified*****")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("*****test_valid_admin_login started*****")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp= Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        # act_dashboard_text = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
        # if act_dashboard_text == "Just a moment...":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
        #     self.driver.close()
        #     assert False
        actual_title = self.driver.title
        exp_title = "Just a moment..."
        if actual_title == exp_title:
            self.logger.info("*****admin logged in*****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp= Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_msg=self.driver.find_element(By.XPATH,"//*[@id='Email-error']").text
        if error_msg=="Please enter a valid email address.":
            self.logger.info("*****invalid admin*****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            assert False