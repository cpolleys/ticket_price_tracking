import asyncio
from playwright.async_api import async_playwright

url = 'https://www.stubhub.com/boston-red-sox-boston-tickets-8-22-2026/event/159260973/?backUrl=%2Fboston-red-sox-tickets%2Fperformer%2F4322&quantity=2'
    
async def scrape_stubhub_redsox():
    async with async_playwright() as p:

        context = await p.chromium.launch_persistent_context(
            user_data_dir="stubhub_profile",
            channel="chrome",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )
        await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """)
            
        page = context.pages[0] if context.pages else await context.new_page()

        page.on("console", lambda msg: print(msg.text))

        
        await page.add_init_script("""
        (() => {
            const originalJson = Response.prototype.json;

            Response.prototype.json = async function () {
                const data = await originalJson.apply(this, arguments);

                try {
                    const str = JSON.stringify(data);

                    if (
                        str.includes("listing") &&
                        str.includes("price") &&
                        str.includes("section")
                    ) {
                        console.log("===== JSON RESPONSE CAUGHT =====");
                        console.log(str.slice(0, 4000));
                    }
                } catch(e){}

                return data;
            };
        })();
        """)
        
        await page.goto(url)
        while True:
            try:
                btn = page.locator('button:has-text("Show more")')
                await btn.click(timeout=2000)
                await page.wait_for_timeout(2000)
            except:
                print("No more listings.")
                break
        
        #data = await page.evaluate("""
        #() => {
            #return Object.keys(window);
        #}
        #""")

        await context.close()
if __name__ == "__main__":
    asyncio.run(scrape_stubhub_redsox())