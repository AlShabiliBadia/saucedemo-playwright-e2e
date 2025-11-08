from playwright.sync_api import Page, expect

class CheckoutStepTwoPage:

    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.page_title = page.locator(".title")
        self.summary_total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("[data-test='finish']")

    def assert_on_checkout_step_two_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
        expect(self.page_title).to_have_text("Checkout: Overview")

    def assert_item_in_overview(self, product_name: str):
        item_container = self.page.locator(".cart_item").filter(has_text=product_name)
        expect(item_container).to_be_visible()

    def get_total_price(self) -> str:
        return self.summary_total_label.text_content()

    def click_finish(self):
        self.finish_button.click()