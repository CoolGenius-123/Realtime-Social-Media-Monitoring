from transformers import pipeline
import pandas as pd
import sqlite3
from databasewrite import write_text_sentiment

def sentiment_analysis(df, search):

    # Create a Sentiment Analysis pipeline
    sentiment_analysis_classifier = pipeline('sentiment-analysis')

    # Sentiment Analysis on datsocial
    df['Sentiment'] = df['posts'].apply(lambda x: sentiment_analysis_classifier(x)[0]['label'])

    # Saving the dataframe
    dbname ="D:/Programming1/Python/web-scraping/Social_media_monitoring/social_media_monitoring.db"

    search = search.replace(" ", "") + "_text_sentiment_table"
    
    write_text_sentiment(dbname, search, df)

    # No. of positive, negative and neutral tweets
    print(df['Sentiment'].value_counts())
    total_negative = len(df[df['Sentiment'] == 'NEGATIVE'])
    total_positive = len(df[df['Sentiment'] == 'POSITIVE'])

    # No of Reddits with positive, negative and neutral sentiment
    print("For Reddit")
    print(df[df['social'] == 'Reddit']['Sentiment'].value_counts())
    total_reddit_negative = len(df[(df['social'] == 'Reddit') & (df['Sentiment'] == 'NEGATIVE')])
    total_reddit_positive = len(df[(df['social'] == 'Reddit') & (df['Sentiment'] == 'POSITIVE')])

    # No of Tweets with positive, negative and neutral sentiment
    print("For Twitter")
    print(df[df['social'] == 'Twitter']['Sentiment'].value_counts())
    total_twitter_negative = len(df[(df['social'] == 'Twitter') & (df['Sentiment'] == 'NEGATIVE')])
    total_twitter_positive = len(df[(df['social'] == 'Twitter') & (df['Sentiment'] == 'POSITIVE')])


    # No of Quora Answers with positive, negative and neutral sentiment
    print("For Quora")
    print(df[df['social'] == 'Quora']['Sentiment'].value_counts())
    total_quora_negative = len(df[(df['social'] == 'Quora') & (df['Sentiment'] == 'NEGATIVE')])
    total_quora_positive = len(df[(df['social'] == 'Quora') & (df['Sentiment'] == 'POSITIVE')])


    # No of Facebook Posts with positive, negative and neutral sentiment
    print("For Facebook")
    print(df[df['social'] == 'Facebook']['Sentiment'].value_counts())
    total_facebook_negative = len(df[(df['social'] == 'Facebook') & (df['Sentiment'] == 'NEGATIVE')])
    total_facebook_positive = len(df[(df['social'] == 'Facebook') & (df['Sentiment'] == 'POSITIVE')])

    # Score According to Sentiment
    score = (total_positive/(total_positive+total_negative))*10

    new_negative = 0
    new_positive = 0


    return [total_negative, total_positive, total_facebook_negative, total_facebook_positive, total_twitter_negative, total_twitter_positive, total_reddit_negative, total_reddit_positive, total_quora_negative, total_quora_positive, score]