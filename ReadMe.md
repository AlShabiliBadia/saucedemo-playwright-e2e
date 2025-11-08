# SauceDemo E2E Test Framework

This is a test automation project for the [SauceDemo](https://www.saucedemo.com/) website, built with Playwright and Pytest.

## Purpose

This project demonstrates how to build a simple, data-driven E2E test framework. It's intended for portfolio use to show skills in web automation, CI/CD, and reporting.

---

## What It Tests

This framework covers the main user flows of the SauceDemo site:

- **Login:** Runs 10 different data-driven scenarios from a JSON file (valid users, locked-out user, invalid credentials, blank fields).
- **Inventory:** Verifies all 4 product sorting options (A-Z, Z-A, Price Low-High, Price High-Low).
- **End-to-End Checkout:** A complete test that simulates a user logging in, adding an item to the cart, filling out checkout information, and successfully placing an order.

---

## Tech Stack

- **Language:** Python
- **Browser Automation:** Playwright
- **Test Runner:** Pytest
- **Reporting:** Allure Reports
- **CI/CD:** GitHub Actions

---

## How to Run Locally

1. **Clone the repository:**

   ```
   git clone https://github.com/AlShabiliBadia/saucedemo-playwright-e2e
   cd saucedemo-playwright-e2e
   ```

2. **Set up a virtual environment:**

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Install Playwright's browsers:**

   ```
   playwright install
   ```

5. **Run tests & generate Allure results:**

   ```
   python -m pytest --alluredir=allure-results --clean-alluredir
   ```

6. **View the HTML report:**

   ```
   allure serve allure-results
   ```
