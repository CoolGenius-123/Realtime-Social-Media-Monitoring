import smtplib
import ssl
from email.message import EmailMessage

def send_email(rows, email_receiver, search):


    # Define email sender and receiver
    email_sender = ''
    email_password = ''

    # Set the subject and body of the email
    subject = 'Sentiment Analysis Report For Your Brand'
    body = f"""
    1. Your company score is {rows[-1]} out of 10,
    2. We have anlysed it by scranning around {rows[0] + rows[1]} tweets and posts on {search} on social media From Twitter, Facebook, Reddit, Quora.
    3. We have found total {rows[1]} positive tweets and posts and total {rows[0]} negative tweets and posts.
    4. From Facebook we have found total {rows[3]} positive posts and total {rows[2]} negative posts.
    5. From Twitter we have found total {rows[5]} positive tweets and total {rows[4]} negative tweets.
    6. From Reddit we have found total {rows[7]} positive posts and total {rows[6]} negative posts.
    7. From Quora we have found total {rows[9]} positive answers and total {rows[8]} negative answers.
    Thank You For Using  Telaverge Communications Services Check Again
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
