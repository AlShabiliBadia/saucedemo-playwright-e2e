from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.page = page
    
        self.page_title = page.locator(".title")
        self.cart_item = page.locator(".cart_item")
        self.item_name = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("[data-test='checkout']")

    def assert_on_cart_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        expect(self.page_title).to_have_text("Your Cart")

    def assert_item_in_cart(self, product_name: str):
        item_container = self.cart_item.filter(has_text=product_name)
        expect(item_container).to_be_visible()
        
        name_element = item_container.locator(self.item_name)
        expect(name_element).to_have_text(product_name)

    def click_checkout(self):
        self.checkout_button.click()