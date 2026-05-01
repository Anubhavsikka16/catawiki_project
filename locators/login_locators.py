class LoginLocators:
    SIGN_IN_BUTTON = "text=/Sign ?In/i"
    
    EMAIL_INPUT = "input[name='email']"
    PASSWORD_INPUT = "input[name='password']"
    
    SUBMIT_BUTTON = "button[type='submit']"

    # Fallback locators
    EMAIL_FALLBACK = "input[type='email']"
    PASSWORD_FALLBACK = "input[type='password']"