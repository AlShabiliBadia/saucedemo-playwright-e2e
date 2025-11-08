from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")
        
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
        
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_login_success(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_login_failure(self, expected_error: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(expected_error)