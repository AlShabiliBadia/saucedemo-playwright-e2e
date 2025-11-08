from playwright.sync_api import Page, expect

class CheckoutStepOnePage:

    def __init__(self, page: Page):
        self.page = page
        
        self.page_title = page.locator(".title")
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")

    def assert_on_checkout_step_one_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
        expect(self.page_title).to_have_text("Checkout: Your Information")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
    
    def click_continue(self):
        self.continue_button.click()