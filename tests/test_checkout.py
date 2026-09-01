"""
test_checkout.py - Tests for the Checkout flow.

These tests use the Page Object Model (POM) to ensure clean, readable,
and maintainable tests without raw selectors.
"""

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import test_data.test_data as td


def test_checkout_page_loads(page: Page):
    """Test 1: Verify the Checkout page loads successfully from the Cart."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.verify_checkout_page_is_displayed()


def test_complete_successful_order(page: Page):
    """Test 2: Verify a complete, successful order flow."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_information(td.FIRST_NAME, td.LAST_NAME, td.POSTAL_CODE)
    checkout_page.click_continue()
    
    checkout_page.verify_overview_page_is_displayed()
    assert checkout_page.is_product_in_overview(td.BACKPACK) is True
    
    checkout_page.click_finish()
    checkout_page.verify_order_confirmation()


def test_checkout_missing_first_name(page: Page):
    """Test 3: Verify validation when first name is missing."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_information("", td.LAST_NAME, td.POSTAL_CODE)
    checkout_page.click_continue()
    checkout_page.verify_error_message("Error: First Name is required")


def test_checkout_missing_last_name(page: Page):
    """Test 4: Verify validation when last name is missing."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_information(td.FIRST_NAME, "", td.POSTAL_CODE)
    checkout_page.click_continue()
    checkout_page.verify_error_message("Error: Last Name is required")


def test_checkout_missing_postal_code(page: Page):
    """Test 5: Verify validation when postal code is missing."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_information(td.FIRST_NAME, td.LAST_NAME, "")
    checkout_page.click_continue()
    checkout_page.verify_error_message("Error: Postal Code is required")


def test_multiple_product_checkout(page: Page):
    """Test 6: Verify checkout flow with multiple products."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.add_product_to_cart(td.BIKE_LIGHT)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.click_checkout()
    
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_information(td.FIRST_NAME, td.LAST_NAME, td.POSTAL_CODE)
    checkout_page.click_continue()
    
    assert checkout_page.is_product_in_overview(td.BACKPACK) is True
    assert checkout_page.is_product_in_overview(td.BIKE_LIGHT) is True
    
    checkout_page.click_finish()
    checkout_page.verify_order_confirmation()
