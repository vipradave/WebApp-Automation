"""
test_products_and_cart.py - Tests for the Products and Cart pages.

These tests demonstrate the Page Object Model (POM) in action.
No raw selectors are used in the tests.
"""

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import test_data.test_data as td


def test_products_page_displayed(page: Page):
    """Test 1: Verify Products page is displayed after login."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.verify_page_is_displayed()


def test_add_product_to_cart(page: Page):
    """Test 2: Verify a product can be added to the cart."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    assert products_page.get_cart_count() == "1"
    
    products_page.open_cart()
    cart_page = CartPage(page)
    assert cart_page.is_product_in_cart(td.BACKPACK) is True


def test_remove_product(page: Page):
    """Test 3: Verify a product can be removed from the cart."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    assert cart_page.is_product_in_cart(td.BACKPACK) is True
    
    cart_page.remove_product(td.BACKPACK)
    assert cart_page.is_product_in_cart(td.BACKPACK) is False


def test_multiple_products(page: Page):
    """Test 4: Verify multiple products can be added to the cart."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.add_product_to_cart(td.BIKE_LIGHT)
    assert products_page.get_cart_count() == "2"
    
    products_page.open_cart()
    cart_page = CartPage(page)
    assert cart_page.is_product_in_cart(td.BACKPACK) is True
    assert cart_page.is_product_in_cart(td.BIKE_LIGHT) is True


def test_product_remains_in_cart_after_navigation(page: Page):
    """Test 5: Verify product remains in cart after navigating away and back."""
    login_page = LoginPage(page)
    login_page.login(td.VALID_USERNAME, td.VALID_PASSWORD)
    
    products_page = ProductsPage(page)
    products_page.add_product_to_cart(td.BACKPACK)
    products_page.open_cart()
    
    cart_page = CartPage(page)
    assert cart_page.is_product_in_cart(td.BACKPACK) is True
    
    # Navigate back to products page
    page.go_back()
    products_page.verify_page_is_displayed()
    assert products_page.get_cart_count() == "1"
    
    # Navigate back to cart
    products_page.open_cart()
    assert cart_page.is_product_in_cart(td.BACKPACK) is True
