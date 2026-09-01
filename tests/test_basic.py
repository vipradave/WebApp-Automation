"""
test_basic.py - A simple beginner test using Playwright and Pytest.

This test does the following:
  1. Opens the Sauce Demo website in a browser
  2. Checks that the page loaded successfully
  3. Verifies the page title is correct
  4. Closes the browser automatically (handled by pytest-playwright)

No Page Object Model is used here — this is a learning exercise!
"""

import re
from playwright.sync_api import Page, expect


def test_page_loads_successfully(page: Page):
    """
    Test 1: Verify that the Sauce Demo website loads successfully.

    The 'page' argument is automatically provided by pytest-playwright.
    It launches a browser, creates a new page, and closes everything
    after the test finishes — no manual setup or teardown needed!
    """

    # Navigate to the Sauce Demo website
    page.goto("https://www.saucedemo.com/")

    # Verify that the login button is visible on the page.
    # If this element is visible, it means the page loaded successfully.
    login_button = page.locator("#login-button")
    expect(login_button).to_be_visible()


def test_page_has_correct_title(page: Page):
    """
    Test 2: Verify that the page title is 'Swag Labs'.

    Playwright's 'expect' function provides helpful assertion methods
    that automatically wait and retry, which makes tests more reliable
    than doing a simple == comparison.
    """

    # Navigate to the Sauce Demo website
    page.goto("https://www.saucedemo.com/")

    # Verify the page title matches "Swag Labs"
    expect(page).to_have_title(re.compile("Swag Labs"))
