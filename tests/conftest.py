"""
Pytest configuration for test automation.
"""
import re
from pathlib import Path

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest_asyncio.fixture(
    scope="session",
    loop_scope="session",
    params=["chromium", "firefox", "edge"],
)
async def browser(request):
    """Create a Playwright browser instance for the session."""
    async with async_playwright() as p:
        if request.param == "edge":
            browser = await p.chromium.launch(channel="msedge", headless=False)
        else:
            browser_type = getattr(p, request.param)
            browser = await browser_type.launch(headless=False)
        yield browser
        await browser.close()


@pytest_asyncio.fixture(loop_scope="session")
async def page(browser, request):
    """Create a new page for each test."""
    page = await browser.new_page()
    try:
        yield page
    finally:
        try:
            if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
                screenshot_dir = Path(__file__).parent / "test-results"
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)
                screenshot_path = screenshot_dir / f"{filename}.png"
                await page.screenshot(path=str(screenshot_path), full_page=True)
                print(f"\nFailure screenshot saved to: {screenshot_path}")
        finally:
            await page.close()

@pytest.fixture
def test_url():
    """Return the base URL for testing."""
    return "http://localhost:8000"
