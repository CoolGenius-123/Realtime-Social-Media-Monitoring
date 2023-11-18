from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import json
from urllib.parse import quote
import threading

def twitter(search, stored, no_post):
    search = quote(search)
    login_url = "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D"

    url = f"https://twitter.com/search?q={search}%20lang%3Aen%20until%3A2023-11-30%20since%3A2023-07-01%20-filter%3Alinks&src=recent_search_click&f=live"

    if no_post > 25:
        no_post = 25

    with sync_playwright() as p:
        page = p.chromium.launch().new_page()
        page.goto(login_url)
        page.wait_for_load_state("networkidle")
        page.fill("input[name='text']", "kh708841@gmail.com")
        page.keyboard.press("Enter")
        page.wait_for_load_state("networkidle")
        try:
            page.fill('input[name="text"]', "@john85465")
            page.keyboard.press("Enter")
            page.wait_for_load_state("networkidle")
            page.fill("input[name='password']", "C++program@123")
            page.keyboard.press("Enter")
            page.wait_for_load_state("networkidle")
        except Exception as e:
            page.fill("input[name='password']", "C++program@123")
            page.keyboard.press("Enter")
            page.wait_for_load_state("networkidle")

        print("Logged in")
        time.sleep(5)
        page.goto(url)
        # page.wait_for_load_state("networkidle")
        time.sleep(2)

        for post in range(1, no_post):
            combine = {}
            try:
                page.wait_for_selector('div[data-testid="cellInnerDiv"]:nth-child({})'.format(post), timeout=3000)
                post_text = page.query_selector(f'div[data-testid="cellInnerDiv"]:nth-child({post}) div[data-testid="tweetText"]')
                if post_text is not None:
                    stored.append(tuple(["Twitter", str(post_text.text_content())]))
                page.keyboard.press("PageDown")
                time.sleep(1)
            
            except Exception as e:
                continue
        return stored

# stored = []
# search = "tcs"
# twitter(search, stored)
# print(stored)