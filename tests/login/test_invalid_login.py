from pages.login_page import LoginPage
from utils.constants import INVALID_USERNAME, INVALID_PASSWORD

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    # Add assertions for invalid login, like checking for an error message
