from playwright.sync_api import sync_playwright
import json

url = 'https://www.stubhub.com/boston-red-sox-tickets/performer/4322?=&PCID=PSUSADWHOME676766076B3973&MetroRegionID=&psc=&ps=&ps_p=0&ps_c=23537388378&ps_ag=193007531277&ps_tg=kwd-2991654073&ps_ad=796631378528&ps_adp=&ps_fi=&ps_li=&ps_lp=1018594&ps_n=g&ps_d=c&ps_ex=&pscpag=kw_intent-2&gcid=C12289X486&utm_source=google&utm_medium=paid-search&utm_sub_medium=prospecting&utm_term=nb&utm_campaign=23537388378:default&utm_content=default&keyword=193007531277_kwd-2991654073_c&creative=796631378528&utm_kxconfid=s2rshsbmv&kwt=nb&mt=e&kw=stubhub%20red%20sox&gad_source=1&gad_campaignid=23537388378&gbraid=0AAAAAD3ylY2hHUsq_WHY8NOH4YWfVX53H&gclid=CjwKCAiAzOXMBhASEiwAe14SaUJ9VHmPUB_EwEFTM-Wl9niRPuwk_sjJP8FoE50gHoraFIqDCWRegBoCSbgQAvD_BwE'

def scrape_stubhub_redox():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)
        # Example scrape (page title for demo)
        title = page.title()
        
        results.append({
            "title": title,
            "url": page.url
        })

        browser.close()
        
        return results

if __name__ == "__main__":
    scrape_stubhub_redox()