from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import json
from urllib.parse import quote
import threading


def quora(search, stored, no_post):
    with sync_playwright() as p:
        page = p.chromium.launch()
        page = page.new_page()
        search = quote(search)
        url = "https://www.quora.com/search?q={}&type=answer".format(search)
        print(url)
        page.goto(url)
        page.wait_for_load_state("networkidle")
        for post in range(1, 5):
            combine = {}
            try:
                page.wait_for_selector('div[class="q-box qu-borderBottom qu-p--medium qu-pb--tiny"]:nth-child({})'.format(post+1), timeout=1000)
                post_text = page.query_selector(f'div[class="q-box qu-borderBottom qu-p--medium qu-pb--tiny"]:nth-child({post+1})')
                posts = post_text.query_selector('div[class="CssComponent__CssInlineComponent-sc-1oskqb9-1 QTextTruncated___StyledCssInlineComponent-sc-1pev100-1  iRsLoo"]')
                page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
                if posts is not None:
                    stored.append(tuple(["Quora", str(posts.text_content())]))
                
            except Exception as e:
                continue
        return stored
    
# values = quora("tcs")
# print(values)

# stored = []
# search = "physics wallah"
# quora(search, stored)
# print(stored)