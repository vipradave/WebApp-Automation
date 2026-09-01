"""
test_login.py - Login tests using Page Object Model.

These tests use the LoginPage class instead of putting raw selectors
directly in the test code. This keeps tests clean and readable.
"""

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import test_data.test_data as td


def test_valid_login(page: Page):
    """Test 1: Verify that a valid user can log in successfully."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    products_page = ProductsPage(page)
    products_page.verify_page_is_displayed()


def test_invalid_login(page: Page):
    """Test 2: Verify that an invalid login shows an error message."""
    login_page = LoginPage(page)
    login_page.login(td.INVALID_USERNAME, td.INVALID_PASSWORD)

    error = login_page.get_error_message()
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match any user in this service")


def test_empty_username(page: Page):
    """Test 3: Verify login behavior with empty username."""
    login_page = LoginPage(page)
    login_page.login("", td.VALID_PASSWORD)

    error = login_page.get_error_message()
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface: Username is required")


def test_empty_password(page: Page):
    """Test 4: Verify login behavior with empty password."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, "")

    error = login_page.get_error_message()
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface: Password is required")


def test_locked_out_user(page: Page):
    """Test 5: Verify login behavior with locked out user."""
    login_page = LoginPage(page)
    login_page.login(td.LOCKED_USERNAME, td.LOCKED_PASSWORD)

    error = login_page.get_error_message()
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
