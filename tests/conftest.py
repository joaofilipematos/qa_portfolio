"""
Pytest configuration for test automation.
"""
import pytest
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
async def browser():
    """Create a Playwright browser instance for the session."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()


@pytest.fixture
async def page(browser):
    """Create a new page for each test."""
    page = await browser.new_page()
    yield page
    await page.close()


@pytest.fixture
def test_url():
    """Return the base URL for testing."""
    return "http://localhost:8000"
