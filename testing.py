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

subreddit="AITAH"

limit = 1

csv_filename = 'reddit_scraper_output.csv'

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Upvotes', 'URL', 'Post Content'])

    # Get the subreddit
    subreddit = reddit.subreddit(subreddit)

    for submission in subreddit.top(limit=limit):
        title = submission.title
        upvotes = submission.score
        url = submission.url
        post=submission.selftext

        writer.writerow([title, post])

        print(f"Title: {title}")
        print(f"Upvotes: {upvotes}")
        print(f"URL: {url}")
        print(f"POST: {post}")
        print("-" * 40)
        time.sleep(2)