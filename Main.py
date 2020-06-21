import praw

#SaleNotifyBot
#CoolFancyBot53!

reddit = praw.Reddit(client_id='cDON-kXRD8QG5g',
                     client_secret='8zNEZKBsRX3bSNDh31Z8k-f21Fs',
                     username="SaleNotifyBot",
                     password="CoolFancyBot53!",
                     user_agent='msg bot by u/xd-Drewski13')


def scansub(sub):

    keywords = ["weed", "people"]

    for submission in reddit.subreddit(sub).stream.submissions():
        # print(submission.title)
        # print(submission.author)
        author = submission.author
        rawtitle = submission.title
        title = rawtitle.split()
        flair = submission.link_flair_text
        if set(keywords) & set(title):
            print(rawtitle)
        else:
            pass


while True:

    scansub("askreddit")
    scansub("pics")