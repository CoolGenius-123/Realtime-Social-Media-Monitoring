# Real-Time Web Scraping for Sentiment Analysis of Any Brand Name using Multi Threading

## Overview - Realtime Web Scrapping and Doing Sentiment Analysis and Any Brand Names or Anything and Alerting the Email User on Any Changes

## Purpose - To Do Sentiment Analysis and No of Posts or Comments of Anything Brand Name or Anything Searched By User and Alert Any Changes according to it.

## Prerequisites

Programming Languages : Python

Important Libaries Used : tranformers, playwright, sqlite3, pandas, smtlib and etc mentioned in Requirements.txt file

Knowledge of Web Scraping is Required.
Knowledge of Playwright is Needed.

## Setup

Virtual Environment : Optional
Needed : Python > 3.9+ of Higher.

## Implementation

1. Playwright Setup

    Install Playwright : pip install playwright && playwright install chromium
    Browser Configuration : used chromium if possible
    Headless Mode : False
    Used it For : Web Automation Like Login to Website Like Twitter, Facebook or LinkedIn and also for scraping site context after login (if needed).

2. Pandas Setup

    Installation: pip install pandas
    Used for : Data Manipulation and Creating DataFrame and also Sentiment Analysis.

3. SQLite Setup (Comes Prebuilt with Python)

    Install: (Optional) Try to install dbbrowser to see the changes in table.
    Used for : Storing Scrapped Data, and also Sentiment Data.

4. Transformers Setup 

    Installation : pip install transformers
    Setup : pipeline('sentiment analysis')
    Used for : Sentiment Analysis Implementation of Scrapped Text

5. Multi-Threading Setup
    
    Used for : Paralled Processing of multiples Threads of Web Scrapper Running at same time.



6. Facebook Scraping Module

    Important : Need to Create Facebook Login Account
    Scrapping : Extracting Live Posts of Latest Searched Brands or Names
    Storing Data : SQlite3 database
    API: Not used any kind of API
    No of Post Can Scrapped: More than 10000+ (No limit)

7. Twitter Scraping Module

    Important : Need to Create Twitter Login Account
    Scrapping : Extracting Live Posts of Latest Searched Brands or Names
    Storing Data : SQlite3 database
    API: Not used any kind of API
    No of Post Can Scrapped: More than 10000+ (No limit)

8.  Reddit Scraping Module

    Important : No Need to Create  Login Account or Anything
    Scrapping : Extracting Live Posts of Latest Searched Brands or Names
    Storing Data : SQlite3 database
    API: Not used any kind of API
    No of Post Can Scrapped: More than 10000+ (No limit)


8.  Quora Scraping Module

    Important : No Need to Create  Login Account or Anything
    Scrapping : Extracting Live Posts of Latest Searched Brands or Names
    Storing Data : SQlite3 database
    API: Not used any kind of API
    No of Post Can Scrapped: More than 10000+ (No limit)


## How it Works:
    1. User Need to Run mainfile.py (which will import all modules and in that) which will run 4 threads running parallel to scrape data from reddit, quora, facebook, twitter.

    2. User Need to Search for Any Kind of Brand Name or Anything he wants.

    3. It will ask for email which you want to send the message after calculation of score.

    4. It might Take some time depending on No Post You Want to Scrapped.

    5. It will all store the data in social_media.db database and tables as well.

    6. After calculating the score it will send you the email that how many positive and negative comments or post you got after analyszing.

    7. For Text Sentiment Analysis it uses Machine Learning Model.

Interface: Command Line Interface (But can be implemented in GUI based as well as Web Based.)


Links to Playwright, SQLite3, Pandas, Transformers documentation
