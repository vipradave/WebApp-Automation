"""
products_page.py - Page Object Model for the SauceDemo Products Page.

This page appears after a successful login. It shows the inventory of
products that can be added to the shopping cart.

URL: https://www.saucedemo.com/inventory.html
"""

from playwright.sync_api import Page, expect


class ProductsPage:
    """
    Represents the SauceDemo Products/Inventory page.

    This class holds locators and actions for browsing products
    and adding them to the cart.
    """

    def __init__(self, page: Page):
        """
        Initialize the ProductsPage with a Playwright Page object.

        Args:
            page: The Playwright page object (provided by pytest-playwright).
        """
        self.page = page

        # ── Locators ─────────────────────────────────────────────────
        # Page title (should show "Products" when on the inventory page)
        self.page_title = page.locator(".title")

        # Shopping cart icon/link in the top-right corner
        self.cart_link = page.locator(".shopping_cart_link")

        # Badge on the cart icon that shows the number of items in cart
        self.cart_badge = page.locator(".shopping_cart_badge")

        # All product items on the page
        self.product_items = page.locator(".inventory_item")

    # ── Assertions ───────────────────────────────────────────────────

    def verify_page_is_displayed(self):
        """
        Verify that the Products page is displayed.

        Checks that the page title says "Products". This is useful
        after login to confirm we landed on the right page.
        """
        expect(self.page_title).to_have_text("Products")

    # ── Actions ──────────────────────────────────────────────────────

    def add_product_to_cart(self, product_name: str):
        """
        Add a product to the cart by its name.

        SauceDemo uses data-test attributes on Add-to-Cart buttons.
        The attribute follows a pattern:
            "Sauce Labs Backpack" → data-test="add-to-cart-sauce-labs-backpack"

        We convert the product name to this format to find the button.

        Args:
            product_name: The exact product name, e.g. "Sauce Labs Backpack"
        """
        # Convert product name to the data-test attribute format:
        #   "Sauce Labs Backpack" → "sauce-labs-backpack"
        slug = product_name.lower().replace(" ", "-")

        # Build the selector and click the Add to Cart button
        add_button = self.page.locator(f"[data-test='add-to-cart-{slug}']")
        add_button.click()

    def open_cart(self):
        """Click the shopping cart icon to navigate to the cart page."""
        self.cart_link.click()

    def get_cart_count(self) -> str:
        """
        Get the number displayed on the cart badge.

        Returns the text of the cart badge (e.g. "1", "2").
        Returns an empty string if no badge is visible (cart is empty).
        """
        if self.cart_badge.is_visible():
            return self.cart_badge.text_content()
        return ""
