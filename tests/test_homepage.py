import pytest
from playwright.async_api import expect

# This test file contains smoke tests for the homepage of the portfolio website.
# run this test file using the following command:
# .\venv\Scripts\python.exe -m pytest tests\test_homepage.py -v


#TC01 - Verify that the homepage is visible in different browsers (chromium, firefox, edge)
@pytest.mark.asyncio(loop_scope="session")
async def test_homepage_shows_greeting_in_each_browser(page, test_url):
    await page.goto(test_url)

    greeting = page.get_by_role("heading", name="Hi there, I'm João Matos.", exact=True)
    await expect(greeting).to_be_visible()

#TC02 - Verify that the footer is visible
@pytest.mark.asyncio(loop_scope="session")
async def test_homepage_footer_visibility_in_each_browser(page, test_url):
    await page.goto(test_url)

    footer = page.get_by_role("contentinfo")
    await expect(footer).to_be_visible()

    footer_text = await footer.inner_text()
    assert "©" in footer_text
