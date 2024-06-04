import praw
import config

def get_top_post(subreddit):
    reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                         client_secret=config.REDDIT_CLIENT_SECRET,
                         user_agent=config.REDDIT_USER_AGENT)
    subreddit = reddit.subreddit(subreddit)
    top_post = subreddit.top(limit=1).next()
    return top_post.title, top_post.selftext, top_post.url
