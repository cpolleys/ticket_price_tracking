import asyncio
from playwright.async_api import async_playwright

url = 'https://www.stubhub.com/boston-red-sox-boston-tickets-8-22-2026/event/159260973/?backUrl=%2Fboston-red-sox-tickets%2Fperformer%2F4322&quantity=2'

async def scrape_stubhub_redsox():
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(url)
        
        #Write playwright page to html
        #html = await page.content()
        #with open("playwright_page.html", "w", encoding="utf-8") as f:
            #f.write(html)
            
        await browser.close()
if __name__ == "__main__":
    asyncio.run(scrape_stubhub_redsox())