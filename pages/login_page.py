from pages.base_page import BasePage
from utils.constants import LOGIN_URL

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = LOGIN_URL
        self.username_field = page.locator("input[name='username']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

    def login(self, username, password):
        self.page.goto(self.url)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
