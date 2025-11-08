from playwright.sync_api import Page, expect

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        
        self.page_title = page.locator(".title")
        self.sort_container = page.locator("[data-test='product-sort-container']")
        self.cart_link = page.locator(".shopping_cart_link")
        self.inventory_item = page.locator(".inventory_item")
        self.item_name = page.locator(".inventory_item_name")
        self.item_price = page.locator(".inventory_item_price")
        
    def assert_on_inventory_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(self.page_title).to_have_text("Products")

    def sort_products(self, sort_order: str):
        self.sort_container.select_option(sort_order)

    def add_item_to_cart_by_name(self, product_name: str):
        item_container = self.inventory_item.filter(has_text=product_name)
        
        add_button = item_container.locator("button[id^='add-to-cart-']")
        add_button.click()

    def click_cart_link(self):
        self.cart_link.click()

    def get_product_names(self) -> list[str]:
        return self.item_name.all_text_contents()
    
    def get_product_prices(self) -> list[float]:
        price_texts = self.item_price.all_text_contents()
        return [float(price.replace("$", "")) for price in price_texts]