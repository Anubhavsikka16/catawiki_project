import pytest
from pages.login_page import LoginPage

from configurationData.config import BASE_URL

@pytest.mark.login
def test_login(page, user_data):
    login = LoginPage(page)
    email = user_data["email"]
    password = user_data["password"]
    login.click_on_login_button()
    login.enter_email(email)
    login.enter_password(password)
    login.click_on_submit_button()
    assert page is not None