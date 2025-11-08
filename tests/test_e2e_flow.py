import pytest
from playwright.sync_api import Page, expect


from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from .Utility import load_checkout_data

def test_full_checkout_flow(logged_in_page: Page):

    data = load_checkout_data()
    product_name = data["test_product"]
    user_info = data["test_user"]
    
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_one_page = CheckoutStepOnePage(logged_in_page)
    checkout_two_page = CheckoutStepTwoPage(logged_in_page)
    checkout_complete_page = CheckoutCompletePage(logged_in_page)

    inventory_page.assert_on_inventory_page()
    inventory_page.add_item_to_cart_by_name(product_name)
    inventory_page.click_cart_link()

    cart_page.assert_on_cart_page()
    cart_page.assert_item_in_cart(product_name)
    cart_page.click_checkout()

    checkout_one_page.assert_on_checkout_step_one_page()
    checkout_one_page.fill_information(
        user_info["first_name"],
        user_info["last_name"],
        user_info["postal_code"]
    )
    checkout_one_page.click_continue()

    checkout_two_page.assert_on_checkout_step_two_page()
    checkout_two_page.assert_item_in_overview(product_name)
    checkout_two_page.click_finish()

    checkout_complete_page.assert_on_checkout_complete_page()
    checkout_complete_page.assert_order_success()