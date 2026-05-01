from locators.login_locators import LoginLocators


class LoginPage():
    
    def __init__(self, page):
        self.page=page
        
    def click_on_login_button(self):
        self.page.click(LoginLocators.SIGN_IN_BUTTON)
        
    def enter_email(self, email):
        try:
            self.page.fill(LoginLocators.EMAIL_INPUT, email)
        except:
            self.page.fill(LoginLocators.EMAIL_FALLBACK, email)

    def enter_password(self, password):
        try:
            self.page.fill(LoginLocators.PASSWORD_INPUT, password)
        except:
            self.page.fill(LoginLocators.PASSWORD_FALLBACK, password)

    def click_on_submit_button(self):
        self.page.click(LoginLocators.SUBMIT_BUTTON)        
        
    