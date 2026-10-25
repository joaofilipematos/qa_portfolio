import pytest
from playwright.async_api import expect

# This test file contains tests for the navbar of the portfolio website.
# run this test file using the following command:
# .\venv\Scripts\python.exe -m pytest tests\test_navbar.py -v

#TC01 - Verify navbar visibility in different browsers (chromium, firefox, edge)
@pytest.mark.asyncio(loop_scope="session")
async def test_navbar_visibility_in_each_browser(page, test_url):
    await page.goto(test_url)

    navbar = page.get_by_role("navigation")
    await expect(navbar).to_be_visible()

#TC02 - Verify page logo is visible and loaded correctly in the navbar
@pytest.mark.asyncio(loop_scope="session")
async def test_navbar_logo_visibility_in_each_browser(page, test_url):
    await page.goto(test_url)

    navbar_logo = page.get_by_role("img", name="QA Portfolio Logo")
    await expect(navbar_logo).to_be_visible()
    await expect(navbar_logo).to_have_js_property("complete", True)
    await expect(navbar_logo).not_to_have_js_property("naturalWidth", 0)

#TC03 - Verify navbar links are visible in different browsers (chromium, firefox, edge)
@pytest.mark.asyncio(loop_scope="session")
async def test_navbar_links_visibility_in_each_browser(page, test_url):
    await page.goto(test_url)

    for name in ["Home", "About", "Professional Experience", "Education & Skills"]:
        link = page.get_by_role("link", name=name, exact=True)
        await expect(link).to_be_visible()
