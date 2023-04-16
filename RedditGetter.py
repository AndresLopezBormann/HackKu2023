import os
from dotenv import load_dotenv
import praw
import re

def GetRedditPost(url, num_comments=0):
    load_dotenv()
    #Setup Reddit Getter
    reddit = praw.Reddit(
        client_id = os.getenv("REDDIT_CLIENT_ID"),
        client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent = os.getenv("REDDIT_USER_AGENT"),
        check_for_updates=False,
        comment_kind="t1",
        message_kind="t4",
        redditor_kind="t2",
        submission_kind="t3",
        subreddit_kind="t5",
        trophy_kind="t6",
        oauth_url="https://oauth.reddit.com",
        reddit_url="https://www.reddit.com",
        short_url="https://redd.it",
        ratelimit_seconds=5,
        timeout=16
    )
    
    # Enter The Post
    submission = reddit.submission(url=url)

    content = {}
    content['title'] = submission.title
    content['body'] = re.sub('[^0-9a-zA-Z\.\?,!]+', ' ', submission.selftext).strip()
    content['url'] = submission.permalink
    content['comments'] = []

    for x in submission.comments.list()[:num_comments]:
        content['comments'].append(
            {
            'comment_url': x.permalink,
            'comment_id': x.id,
            'comment_body': re.sub('[^0-9a-zA-Z\.\?,!]+', ' ', x.body).strip(),
            }
        )

    return content