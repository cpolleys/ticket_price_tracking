import asyncio
from playwright.async_api import async_playwright

url = 'https://www.stubhub.com/boston-red-sox-boston-tickets-8-22-2026/event/159260973/?backUrl=%2Fboston-red-sox-tickets%2Fperformer%2F4322&quantity=2'

async def test_json(response):
    if request.resource_type == "fetch":
        print("REQUEST:", request.url)
        #print("XHR:", response.url)
    #try:
        #print(await response.json())
    #except:
        #pass

async def scrape_stubhub_redsox():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        page.on('response', lambda response: test_json(response))
        await page.goto(url)
        await page.mouse.wheel(0, 4000)
        await page.wait_for_timeout(8000)
        
        
        
        #Write playwright page to html
        #html = await page.content()
        #with open("playwright_page.html", "w", encoding="utf-8") as f:
            #f.write(html)
            
        await browser.close()
if __name__ == "__main__":
    asyncio.run(scrape_stubhub_redsox())