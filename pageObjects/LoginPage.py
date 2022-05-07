class LoginPage:
    textbox_username_id = "exampleInputEmail1"
    textbox_password_id = "exampleInputPassword1"
    button_login_id = "login"
    button_claims_xpath = "//button[@xpath='1'>Claims]"
    button_logout_id = "logout"

    # total_claims_id="total_claims"

    def __init__(self, driver):
        self.driver = driver
    
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickClaims(self):
        self.driver.find_element_by_xpath(self.button_claims_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logout_id).click()

    # def total_claims(self):
    #     self.driver.find_element_by_id(self.total_claims_id).text()


