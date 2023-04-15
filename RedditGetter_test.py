from RedditGetter import GetRedditPost

def main():

    num_comments = int(input('Enter the number of comments: '))
    reddit_post = 'https://www.reddit.com/r/scarystories/comments/ijjshz/run/'  

    reddit_object = GetRedditPost(reddit_post, num_comments)

    comments = ''
    for i in range(num_comments):
        comments += f"\n{reddit_object['comments'][i]['comment_body']}"

    Result = f"Title: {reddit_object['title']}\nBody: {reddit_object['body']}\nComments: {comments}"
    
    print(Result)

if __name__ == '__main__':
    main()