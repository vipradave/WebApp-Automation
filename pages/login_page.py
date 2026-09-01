"""
login_page.py - Page Object Model for the SauceDemo Login Page.

What is Page Object Model (POM)?
================================
POM is a design pattern where each web page gets its own Python class.
The class contains:
  - LOCATORS: How to find elements on the page (selectors like #user-name)
  - METHODS:  Actions you can perform on the page (type username, click login)

Why use POM?
  - Keeps selectors out of test files (if a selector changes, fix it in ONE place)
  - Tests read like plain English: login_page.login("user", "pass")
  - Makes tests easier to write, read, and maintain
"""

from playwright.sync_api import Page


class LoginPage:
    """
    Represents the SauceDemo login page at https://www.saucedemo.com/

    This class holds all the locators (element selectors) and actions
    for the login page, so our test files stay clean and simple.
    """

    # ── URL ──────────────────────────────────────────────────────────
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page object.

        Args:
            page: The Playwright page object (provided by pytest-playwright).
        """
        self.page = page

        # ── Locators ─────────────────────────────────────────────────
        # These find elements on the page using CSS selectors.
        # We store them here so they're easy to update if the page changes.
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    # ── Actions ──────────────────────────────────────────────────────
    # Each method performs one action on the page.

    def navigate(self):
        """Open the SauceDemo login page in the browser."""
        self.page.goto(self.URL)

    def enter_username(self, username: str):
        """Type a username into the username field."""
        self.username_field.fill(username)

    def enter_password(self, password: str):
        """Type a password into the password field."""
        self.password_field.fill(password)

    def click_login(self):
        """Click the Login button."""
        self.login_button.click()

    def login(self, username: str, password: str):
        """
        Perform a complete login: navigate to the page, enter credentials,
        and click Login.

        This is a convenience method that combines all the individual steps
        into one easy-to-call method.

        Args:
            username: The username to enter.
            password: The password to enter.
        """
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """
        Return the locator for the error message element.

        We return the locator (not the text) so that the test can use
        Playwright's expect() assertions on it, which automatically
        wait and retry.
        """
        return self.error_message
