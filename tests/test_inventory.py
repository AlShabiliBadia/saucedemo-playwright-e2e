import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from .Utility import load_inventory_data, get_sort_test_id


inventory_data = load_inventory_data()

@pytest.mark.parametrize("scenario", inventory_data["sort_scenarios"], ids=get_sort_test_id)
def test_product_sorting(logged_in_page: Page, scenario: dict):
    inventory_page = InventoryPage(logged_in_page)
    
    sort_order = scenario["sort_order"]
    test_type = scenario["test_type"]
    expected_list = scenario["expected_list"]
    
    inventory_page.sort_products(sort_order)

    if test_type == "names":
        actual_list = inventory_page.get_product_names()
    elif test_type == "prices":
        actual_list = inventory_page.get_product_prices()
    
    assert actual_list == expected_list, f"Sort order {sort_order} failed"

def test_add_item_to_cart(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)
    item_name = inventory_data["item_to_add"]
    
    inventory_page.add_item_to_cart_by_name(item_name)
    
    item_container = inventory_page.inventory_item.filter(has_text=item_name)
    remove_button = item_container.locator("button[id^='remove-']")
    
    expect(remove_button).to_be_visible()
    expect(remove_button).to_have_text("Remove")
    
    cart_badge = inventory_page.cart_link.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")