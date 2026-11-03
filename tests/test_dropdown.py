#Dropdowns
from playwright.sync_api import expect
def test_native_dropdown(page):
    page.goto("https://practice.expandtesting.com/dropdown")
    dropdown = page.locator("#dropdown")
    expect(dropdown).to_be_visible()
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")
    print("dropdown 1 selected")
    dropdown.select_option("2")
    expect(dropdown).to_have_value("2")

    print("dropdown options are selected successfully")