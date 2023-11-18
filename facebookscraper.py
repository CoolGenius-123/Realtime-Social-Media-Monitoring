from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import json
from urllib.parse import quote


def facebook(search, stored, no_post):
    starting_url = 'https://www.facebook.com/'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(starting_url)
        page.wait_for_selector('input[name="email"]')
        page.fill('input[name="email"]', 'kh708841@gmail.com')
        page.fill('input[name="pass"]', 'C++program@123')
        page.click('button[name="login"]')
        page.wait_for_load_state("networkidle")
        search = quote(search)
        page.goto("https://www.facebook.com/search/posts?q={}&filters=eyJyZWNlbnRfcG9zdHM6MCI6IntcIm5hbWVcIjpcInJlY2VudF9wb3N0c1wiLFwiYXJnc1wiOlwiXCJ9IiwicnBfY3JlYXRpb25fdGltZTowIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAyM1xcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAyMy0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDIzXFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAyMy0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMjMtMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMjMtMTItMzFcXFwifVwifSJ9".format(search))
        # stored = []
        post_skip = []
        for post in range(1, no_post):
            try:
                page.wait_for_selector('div[aria-posinset="{}"]'.format(post), timeout=3000)
                post_text = page.query_selector(f'div[aria-posinset="{post}"]')
                try:
                    post_text.click('div[role="button"]')
                    page.wait_for_load_state("networkidle")
                except Exception as e:
                    pass
                
                posts = post_text.query_selector(f'div[aria-posinset="{post}"]')
                stored.append(tuple(["Facebook",post_text.text_content()]))
                page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            except Exception as e:
                post_skip.append(post)
                continue
        return stored
    
# start = time.time()
# name = input("Enter the name of posts to scrape: ")
# stored = []
# vale = facebook(name, stored)
# end = time.time()

# print(vale, len(vale))
