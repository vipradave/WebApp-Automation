"""
cart_page.py - Page Object Model for the SauceDemo Cart Page.

This page displays the products that have been added to the shopping cart.
"""

from playwright.sync_api import Page, expect

class CartPage:
    """
    Represents the SauceDemo Cart page.
    """

    def __init__(self, page: Page):
        """
        Initialize the CartPage with a Playwright Page object.
        """
        self.page = page

        # Page title (should show "Your Cart")
        self.page_title = page.locator(".title")

        # Cart items list
        self.cart_items = page.locator(".cart_item")
        
        # Checkout button
        self.checkout_button = page.locator("[data-test='checkout']")

    def verify_page_is_displayed(self):
        """
        Verify that the Cart page is displayed by checking the page title.
        """
        expect(self.page_title).to_have_text("Your Cart")

    def is_product_in_cart(self, product_name: str) -> bool:
        """
        Check if a specific product is in the cart.
        
        Args:
            product_name: The exact name of the product.
            
        Returns:
            True if the product is found in the cart, False otherwise.
        """
        # Search for the product name within the cart item descriptions
        product = self.cart_items.filter(has_text=product_name)
        return product.count() > 0

    def remove_product(self, product_name: str):
        """
        Remove a product from the cart by clicking its Remove button.
        
        Args:
            product_name: The exact name of the product to remove.
        """
        # Find the specific cart item by text, then find its remove button
        slug = product_name.lower().replace(" ", "-")
        # SauceDemo uses data-test attributes for remove buttons as well
        remove_button = self.page.locator(f"[data-test='remove-{slug}']")
        remove_button.click()

    def click_checkout(self):
        """
        Click the checkout button to proceed to the next step.
        """
        self.checkout_button.click()
