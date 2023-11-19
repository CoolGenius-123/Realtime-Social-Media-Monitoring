# Real-Time Web Scraping for Sentiment Analysis of Any Brand Name using Multi-Threading

## Overview

This project performs real-time web scraping and sentiment analysis on any specified brand name or topic across various social media platforms. It utilizes multi-threading for parallel processing, Playwright for web automation, SQLite for data storage, Pandas for data manipulation, and Transformers for sentiment analysis using a pre-trained model.

## Purpose

The purpose of this project is to provide users with real-time sentiment analysis and the number of posts or comments related to any given brand name or topic. Users are alerted via email in case of any significant changes in sentiment.

## Prerequisites

- **Programming Languages**: Python
- **Libraries**: transformers, playwright, sqlite3, pandas, smtlib, etc. (refer to Requirements.txt)
- **Web Scraping Knowledge**: Playwright
- **Virtual Environment**: Optional
- **Python Version**: 3.9+

## Setup

1. **Playwright Setup**
    - Install Playwright: `pip install playwright && playwright install chromium`
    - Browser Configuration: Use Chromium if possible
    - Headless Mode: False
    - Usage: Web automation for login to websites like Twitter, Facebook, or LinkedIn and site context scraping after login.

2. **Pandas Setup**
    - Installation: `pip install pandas`
    - Usage: Data manipulation, creating DataFrames, and sentiment analysis.

3. **SQLite Setup**
    - Installation: Pre-built with Python
    - Usage: Storing scraped data and sentiment analysis results.

4. **Transformers Setup**
    - Installation: `pip install transformers`
    - Setup: `pipeline('sentiment analysis')`
    - Usage: Implementing sentiment analysis on scraped text.

5. **Multi-Threaded Setup**
    - Usage: Parallel processing of multiple threads for simultaneous web scraping.

6. **Facebook Scraping Module**
    - Prerequisites: Facebook login account
    - Scraping: Extract live posts of the latest searched brands or names
    - Storage: SQLite3 database
    - API: No external API used

7. **Twitter Scraping Module**
    - Prerequisites: Twitter login account
    - Scraping: Extract live posts of the latest searched brands or names
    - Storage: SQLite3 database
    - API: No external API used

8. **Reddit Scraping Module**
    - Prerequisites: No login required
    - Scraping: Extract live posts of the latest searched brands or names
    - Storage: SQLite3 database
    - API: No external API used

9. **Quora Scraping Module**
    - Prerequisites: No login required
    - Scraping: Extract live posts of the latest searched brands or names
    - Storage: SQLite3 database
    - API: No external API used

## How it Works

1. Run `mainfile.py`, which imports all modules and runs four threads in parallel to scrape data from Reddit, Quora, Facebook, and Twitter.

2. Enter the brand name or topic you want to search for.

3. Provide the email address to receive sentiment analysis results.

4. The process may take some time depending on the number of posts to be scraped.

5. Data is stored in the `social_media.db` database and corresponding tables.

6. After calculating the sentiment score, an email is sent detailing the positive and negative comments or posts.

7. For text sentiment analysis, a machine learning model is used.

## Interface

Command Line Interface (CLI) - Can be implemented in GUI or Web-based interfaces.

## Additional Information

- Sentiment Analysis Model: [Transformers documentation](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
