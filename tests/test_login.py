import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page
from .Utility import load_login_data, get_test_id


@pytest.mark.parametrize("scenario", load_login_data(), ids=get_test_id)
def test_login_scenarios(page: Page, scenario: dict):

    login_page = LoginPage(page)
    
    username = scenario.get("username")
    password = scenario.get("password")
    expected_outcome = scenario.get("expected_outcome")
    
    login_page.navigate()
    login_page.login(username, password)

    if expected_outcome == "success":
        login_page.assert_login_success()
    elif expected_outcome == "failure":
        expected_error = scenario.get("expected_error", "Error message not specified")
        login_page.assert_login_failure(expected_error)