import praw
import csv
import time

reddit = praw.Reddit(
    client_id="l8nzxC1a_GSPVDmVR4UI2g",
    client_secret="9RJM4I6RUNPkC_i3RXpQuMQx-LCK1A",
    user_agent="MerMer by /u/Comfortable-Sky6282",
    username="Comfortable-Sky6282",
    password="Aalywbwdy830312@"
)

subreddits=["AITAH","Creepypasta","TwoHotTakes"]

limit=5
for sub in subreddits:
    csv_filename = sub+'_output.csv'


    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(['Title', 'Post Content'])

        subreddit = reddit.subreddit(sub)

        for submission in subreddit.new(limit=limit):
            title = submission.title
            post=submission.selftext

            writer.writerow([title, post])

            print(f"Title: {title}")
            print(f"POST: {post}")
            print("-" * 40)
            time.sleep(2)