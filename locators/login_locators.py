class LoginLocators:
    SIGN_IN_BUTTON = "text=/Sign ?In/i"
    
    EMAIL_INPUT = "#field_r_o_"
    PASSWORD_INPUT = "#field_r_p_"
    
    SUBMIT_BUTTON = "button[type='submit'] span[class='c-button__overlay c-button__overlay--primary']"

    # Fallback locators
    EMAIL_FALLBACK = "input[type='email']"
    PASSWORD_FALLBACK = "input[type='password']"