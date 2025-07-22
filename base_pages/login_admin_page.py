#webelemnts and action methods

from selenium.webdriver.common.by import By


#locators
class Login_Admin_Page:
    username_id="Email"
    password_id="Password"
    login_xpath="//button[@type='submit']"
    link_logout="Logout"

#constructor to accept driver as parameter
    def __init__(self,driver):
        self.driver=driver

#action methods
    def enter_username(self,username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout).click()

