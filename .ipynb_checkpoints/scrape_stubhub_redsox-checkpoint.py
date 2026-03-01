import asyncio
from playwright.async_api import async_playwright

url = 'https://www.stubhub.com/boston-red-sox-boston-tickets-8-22-2026/event/159260973/?backUrl=%2Fboston-red-sox-tickets%2Fperformer%2F4322&quantity=2'

async def log_requests(request):
    if request.resource_type == "fetch" and request.method == "POST":
        print("\nPOST:", request.url)
        if request.post_data:
            print(request.post_data[:400])  # preview

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
        browser = await p.chromium.launch(headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        ))
        context = await browser.new_context(
            viewport={"width":1280,"height":800},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """)
        page = await context.new_page()

        page.on("request", log_requests)
        #page.on('response', lambda response: test_json(response))
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