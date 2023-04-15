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