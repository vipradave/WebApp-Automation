"""
checkout_page.py - Page Object Model for the SauceDemo Checkout flow.

This page handles the entire checkout process, including:
1. Your Information
2. Overview
3. Complete
"""

from playwright.sync_api import Page, expect

class CheckoutPage:
    """
    Represents the SauceDemo Checkout pages.
    """

    def __init__(self, page: Page):
        """
        Initialize the CheckoutPage with a Playwright Page object.
        """
        self.page = page

        # General Title locator (used across different checkout steps)
        self.page_title = page.locator(".title")

        # Step 1: Your Information Locators
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.cancel_button = page.locator("[data-test='cancel']")
        self.error_message = page.locator("[data-test='error']")

        # Step 2: Overview Locators
        self.cart_items = page.locator(".cart_item")
        self.finish_button = page.locator("[data-test='finish']")

        # Step 3: Complete Locators
        self.confirmation_header = page.locator(".complete-header")


    def verify_checkout_page_is_displayed(self):
        """
        Verify that the first step of checkout (Your Information) is displayed.
        """
        expect(self.page_title).to_have_text("Checkout: Your Information")

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str):
        """
        Fill in the customer information form.
        """
        # We use fill() to input text, which also clears the field first
        if first_name:
            self.first_name_input.fill(first_name)
        if last_name:
            self.last_name_input.fill(last_name)
        if postal_code:
            self.postal_code_input.fill(postal_code)

    def click_continue(self):
        """
        Click the continue button to proceed to the overview page.
        """
        self.continue_button.click()
        
    def verify_error_message(self, expected_text: str = None):
        """
        Verify that an error message is visible. Optionally verify the text.
        """
        expect(self.error_message).to_be_visible()
        if expected_text:
            expect(self.error_message).to_contain_text(expected_text)

    def verify_overview_page_is_displayed(self):
        """
        Verify that the second step of checkout (Overview) is displayed.
        """
        expect(self.page_title).to_have_text("Checkout: Overview")

    def is_product_in_overview(self, product_name: str) -> bool:
        """
        Check if a specific product is present in the order overview.
        """
        product = self.cart_items.filter(has_text=product_name)
        return product.count() > 0

    def click_finish(self):
        """
        Click the finish button to complete the order.
        """
        self.finish_button.click()

    def verify_order_confirmation(self):
        """
        Verify that the order confirmation page is displayed and shows the success message.
        """
        expect(self.page_title).to_have_text("Checkout: Complete!")
        expect(self.confirmation_header).to_have_text("Thank you for your order!")
