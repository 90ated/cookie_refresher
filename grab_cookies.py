import json
from playwright.sync_api import sync_playwright

def save_cookies(url: str, output_file: str = "cookies.json"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context()

        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state("load")

        cookies = context.cookies()

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=4)

        browser.close()
        print(f"Saved {len(cookies)} cookies to {output_file}")

if __name__ == "__main__":
    save_cookies("https://trends.google.com/trends/")
