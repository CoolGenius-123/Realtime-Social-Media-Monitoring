from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import json
from urllib.parse import quote
import threading


def reddit(search, stored, no_post):
    search = search.split()
    search = "+".join(search)
    url = 'https://www.reddit.com/search/?q={}&type=link&cId=fa555978-4b59-4e5b-9db7-506518e53b8a&iId=7cf1ecff-f5f8-47e9-8dcb-219948a8b0e1&sort=new'.format(search)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('faceplate-tracker[aria-posinset="1"]')
        for post in range(1, no_post):
            combine = {}
            try:
                page.wait_for_selector('faceplate-tracker[aria-posinset="{}"]'.format(post), timeout=3000)
                post_text = page.query_selector(f'faceplate-tracker[aria-posinset="{post}"]')
                page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
                posts = post_text.query_selector("span[class='invisible']")
                if posts is not None:
                    # combine["Reddit"] = posts.text_content()
                    stored.append(tuple(["Reddit", str(posts.text_content())]))
            except Exception as e:
                continue
        return stored

# values = reddit("tcs")
# print(values)

# search = "tcs".lower()
# stored = []
# reddit(search, stored)
# print(stored, type(stored))