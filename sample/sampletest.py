import pytest
from playwright.sync_api import Page, expect

def test_ecommerce(page: Page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Signup / Login").click()
    page.locator('[data-qa="signup-name"]').fill("testuser")
    page.locator('[data-qa="signup-email"]').fill("abctest@gmail.com")
    