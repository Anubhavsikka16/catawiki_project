from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from configurationData.config import Config

class LoginPage(BasePage):
    
    def __init__(self, page):
        self.page=page
        
     
    def click_on_login_button(self):
        self.accept_cookies()
        self.click(css="div[class='tw:hidden tw:md:block'] span[class='c-button__overlay c-button__overlay--primary']")
        
    def enter_email(self, email):
        try:
            self.fill(value=Config.TEST_EMAIL, label="Email address")
        except:
            self.fill(LoginLocators.EMAIL_FALLBACK, email)
        #self.page.get_by_label("Email address").fill(Config.TEST_EMAIL)
    def enter_password(self, password):
        try:
            self.fill(value=Config.TEST_PASSWORD, label="Password")
        except:
            self.fill(LoginLocators.PASSWORD_FALLBACK, password)

    def click_on_submit_button(self):
        self.click(css= "button[type='submit'] span[class='c-button__overlay c-button__overlay--primary']")       
        
    