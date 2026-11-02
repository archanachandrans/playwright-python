#Run Command
#python -m pytest tests/test_codegen.py -v --tracing retain-on-failure --screenshot only-on-failure --output=test-results

# from playwright.sync_api import sync_playwright, expect

# from playwright.sync_api import Page, expect

# def test_login(page: Page) -> None:

#     page.goto("https://www.saucedemo.com/")

#     page.locator('[data-test="username"]').fill("standard_user")

#     page.locator('[data-test="password"]').fill("secret_sauce")

#     page.locator('[data-test="login-button"]').click()

#     expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")


#End to end testing
#Reusable functions -- Write code once and use it across multiple tests
#Test data -- Use different input to test the same workflow

#API mocking -- simulate API response without actually calling the backend service

#End to End workflow
#Workflow is a sequence of actions that user performs to accomplish a task

#tests/test_login.py:

import pytest

from playwright.sync_api import Page, expect
from test_data.login_data import LOGIN_TEST_DATA

@pytest.mark.parametrize("test_data", LOGIN_TEST_DATA)

def test_login(page: Page, test_data: dict) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill(test_data["username"])
    page.locator('[data-test="password"]').fill(test_data["password"])
    page.locator('[data-test="login-button"]').click()
    if test_data["expected"] == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator('[data-test="error"]')).to_be_visible()
