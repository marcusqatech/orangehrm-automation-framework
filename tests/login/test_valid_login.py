from pages.login_page import LoginPage
from utils.constants import USERNAME, PASSWORD

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    # Add assertions for valid login, like checking the dashboard visibility
