class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for()
