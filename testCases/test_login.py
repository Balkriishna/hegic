import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
# import org.openqa.selenium.support.Color
from selenium.webdriver.support.color import Color




class Test_001_Login:
    baseURL = "https://hegic.portal.camcom.ai/login"
    username = "jatin@gmail.com"
    password = "password"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        time.sleep(5)
        if act_title == "ADDA Portal for Client":
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickClaims()
        time.sleep(5)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "ADDA Portal for Client":
            assert True
        else:
            assert False

#Claims Xpath //button[@xpath="1">Claims]

    # def claims_test(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     claims=self.lp.total_claims()
    #     print(claims)
    #     self.driver.close()



