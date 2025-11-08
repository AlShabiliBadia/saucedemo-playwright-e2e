from playwright.sync_api import Page, expect

class CheckoutCompletePage:

    def __init__(self, page: Page):
        self.page = page
        
        self.page_title = page.locator(".title")
        self.complete_header = page.locator(".complete-header")

    def assert_on_checkout_complete_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
        expect(self.page_title).to_have_text("Checkout: Complete!")

    def assert_order_success(self):
        expect(self.complete_header).to_be_visible()
        expect(self.complete_header).to_have_text("Thank you for your order!")