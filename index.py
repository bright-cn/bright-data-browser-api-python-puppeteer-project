#!/usr/bin/env python3
"""
Example of using Bright Data scraping browser with pyppeteer
This simple script demonstrates how to make a request to a website through Bright Data scraping Browser
"""
import asyncio
import os
from pyppeteer import connect

# STEP 1: Configure your Bright Data scraping browser endpoint
#  - Get endpoint from: https://brightdata.com/cp/zones
#  - Create new scraping browser: https://docs.brightdata.com/scraping-automation/scraping-browser/quickstart
#  - Websocket format: wss://brd-customer-[id]-zone-[zone]:[password]@[domain]:[port]
BROWSER_WEBSOCKET_ENDPOINT = os.getenv('BRIGHT_DATA_SCRAPING_BROWSER_WEBSOCKET_ENDPOINT', "wss://brd-customer-hl_e028a59e-zone-scraping_browser1:jl6q3m5tkxxy@brd.superproxy.io:9222")

# STEP 2: Set your target URL
PAGE_URL = "https://example.com"

# STEP 3: Run `python index.py` command in terminal

async def main():
    print("🚀 Starting the scraping process...")
    browser = None
    
    try:
        print("🌐 Connecting to the Scraping Browser...")
        browser = await connect(browserWSEndpoint=BROWSER_WEBSOCKET_ENDPOINT)
        print("✅ Successfully connected to the browser!")

        page = await browser.newPage()
        print("🌍 Navigating to the test URL...")
        await page.goto(PAGE_URL, {'timeout': 2 * 60 * 1000})  # 2 minutes timeout
        
        print("📸 Taking a screenshot of the page...")
        await page.screenshot({'path': './page.png', 'fullPage': True})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        print("✅ Screenshot saved as 'page.png'!")

        print("🔍 Scraping page content...")
        html = await page.content().                                                                                                                                                                                                                                                                                                                                                                                                                                                           n  
        print("📝 Page content retrieved:")
        print(html)
        
    except Exception as error:
        print("❌ An error occurred during scraping:")
        print(f"Error message: {str(error)}")
        import traceback
        print(f"Stack trace:\n{traceback.format_exc()}")
    finally:
        if browser:
            await browser.close()
            print("👋 Browser closed.")

if __name__ == "__main__":
    asyncio.run(main())