from pages.base_page import BasePage
from utils.constants import DASHBOARD_URL

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = DASHBOARD_URL
        # Locators for elements on the dashboard page
        self.dashboard_header = page.locator("div.orangehrm-dashboard-header h6")
        self.welcome_message = page.locator("div#welcome")
        self.menu_button = page.locator("button#menu-toggle")
        self.quick_launch_panel = page.locator("div.quicklaunch-panel")
        self.recent_reports_section = page.locator("div.recent-reports")
        self.logout_button = page.locator("a#welcome-menu-logout")

    def go_to_dashboard(self):
        """Navigate to the dashboard page."""
        self.page.goto(self.url)

    def check_dashboard_visibility(self):
        """Ensure the dashboard header and welcome message are visible."""
        self.dashboard_header.wait_for()
        self.welcome_message.wait_for()

    def open_menu(self):
        """Click the menu button to open the sidebar."""
        self.menu_button.click()

    def is_quick_launch_panel_visible(self):
        """Check if the Quick Launch Panel is visible on the dashboard."""
        return self.quick_launch_panel.is_visible()

    def is_recent_reports_section_visible(self):
        """Check if the Recent Reports section is visible on the dashboard."""
        return self.recent_reports_section.is_visible()

    def get_welcome_message(self):
        """Retrieve the welcome message text."""
        return self.welcome_message.text_content()

    def logout(self):
        """Log out from the dashboard."""
        self.welcome_message.hover()  # Hover over the welcome message to show the logout option
        self.logout_button.click()
