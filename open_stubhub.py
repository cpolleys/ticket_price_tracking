from playwright.sync_api import sync_playwright
import json

from playwright.sync_api import sync_playwright

URL = "https://www.stubhub.com/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(URL, timeout=60000)
        page.wait_for_timeout(10000)

        browser.close()

if __name__ == "__main__":
    main()