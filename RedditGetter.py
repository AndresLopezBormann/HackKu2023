import os
from dotenv import load_dotenv
import praw
import re

def GetRedditPost(url, num_comments=0):
    """
    GetRedditPost function takes a Reddit post URL and number of comments to return, and returns a dictionary containing
    information about the post and its comments.

    Args:
    url (str): A string containing the URL of the Reddit post.
    num_comments (int): An integer representing the number of comments to return. If set to 0, returns no comments.

    Returns:
    dict: A dictionary containing the following keys:
    - 'title': A string representing the title of the post.
    - 'body': A string representing the body of the post.
    - 'url': A string representing the permalink of the post.
    - 'comments': A list of dictionaries containing information about the comments. Each dictionary contains the following keys:
    - 'comment_url': A string representing the permalink of the comment.
    - 'comment_id': A string representing the ID of the comment.
    - 'comment_body': A string representing the body of the comment.
    """
    load_dotenv()
    #Setup Reddit Getter
    reddit = praw.Reddit(
        client_id = os.getenv("REDDIT_CLIENT_ID"),
        client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent = os.getenv("REDDIT_USER_AGENT"),
    )
    
    # Enter The Post
    submission = reddit.submission(url=url)

    # Creates the Dictionary for the output
    content = {}
    content['title'] = submission.title
    content['body'] = re.sub('[^0-9a-zA-Z\.\?,!]+', ' ', submission.selftext).strip()
    content['url'] = submission.permalink
    content['comments'] = []

    #Loops throught the comments and adds them to the a comments list
    for x in submission.comments.list()[:num_comments]:
        content['comments'].append(
            {
            'comment_url': x.permalink,
            'comment_id': x.id,
            'comment_body': re.sub('[^0-9a-zA-Z\.\?,!]+', ' ', x.body).strip(),
            }
        )

    return content