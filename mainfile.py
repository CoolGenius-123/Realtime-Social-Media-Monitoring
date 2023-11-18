from facebookscraper import facebook
from redditscraper import reddit
from twitterscraper import twitter
from quorascraper import quora
import time
import threading
import json
import pandas as pd
from transformers import pipeline
from email_sender import send_email
from databasewrite import write_data_scrape, write_sentiment_data
import sqlite3
from sentiment import sentiment_analysis


def scraping(search, no_post):
    stored = []
    start = time.time()
    reddit_thread = threading.Thread(target=reddit, args=(search, stored, no_post))
    twitter_thread = threading.Thread(target=twitter, args=(search, stored, no_post))
    quora_thread = threading.Thread(target=quora, args=(search, stored, no_post))
    facebook_thread = threading.Thread(target=facebook, args=(search, stored, no_post))

    reddit_thread.start()
    twitter_thread.start()
    quora_thread.start()
    facebook_thread.start()

    reddit_thread.join()
    twitter_thread.join()
    quora_thread.join()
    facebook_thread.join()

    end = time.time()

    return stored, end-start

def DataFrame(databasename, tablename):

    # Connecting to the database
    conn = sqlite3.connect(databasename)

    # SQL Query
    sql = f"SELECT * FROM {tablename}"

    # Execute the SQL query and load the result into a DataFrame
    df = pd.read_sql_query(sql, conn)

    return df

def start():

    search = input("Enter the search query: ")
    email = input("Enter your email address: ")
    no_post = int(input("Enter the number of post you want to scrape: "))

    # Scraping the data
    data, time_taken = scraping(search, no_post)

    print("Time taken to scrape the data: ", time_taken)

    dbname = 'D:/Programming1/Python/web-scraping/Social_media_monitoring/social_media_monitoring.db'

    tablename = search.replace(" ", "") + "_table"
          
    # Saving the data
    write_data_scrape(databasename=dbname, tablename=tablename, data=data)

    # Create Dataframe from database
    data_frame = DataFrame(databasename=dbname, tablename=tablename)

    print(data_frame.head())

    # Sentiment Analysis
    rows = sentiment_analysis(data_frame, search)

    # Saving the data
    sentimentname = search.replace(" ", "") + "_sentimenttable"
    write_sentiment_data(databasename=dbname, tablename=sentimentname, data=rows)

    print("Sentiment Analysis Completed got Scored {}".format(rows[-1]))

    # Sending the email
    send_email(rows, email, search)
    
    print("Thank you for using our service.")

start()


