import praw
import time

# SaleNotifyBot
# CoolFancyBot53!
# the above are details for the account "SaleNotifyBot" which is used to PM you on reddit.

# you should be able to use your own account for this too but i was unable to test this because my account
# has 2fa enabled and it requires more work to get it working (probably an easy task but oh well lol)

reddit = praw.Reddit(client_id='CuluidDV9j47mA',
                     client_secret='_fIRuRlLs5Xd4M5_5XT61DjLO88',
                     username="SaleNotifyBot",
                     password="CoolFancyBot53!",
                     user_agent='msg bot by u/xd-Drewski13')  # and the reddit police?? hehehehehehe


def scansub(sub):
    # --------- Add your keywords you would like to track here! ---------------
    keywords = ["2080ti", "2070", "intel"]
    # -------------------------------------------------------------------------
    for submission in reddit.subreddit(sub).stream.submissions():
        rawtitle = submission.title
        title = rawtitle.split()
        flair = submission.link_flair_text
        link = submission.permalink
        time.sleep(1)
        if set(keywords) & set(title):
            matchingword = set(keywords) & set(title)
            reddit.redditor('xd-Drewski13').message(f'Match found for a {flair}!',
                                                          f'I have found a post containing your keyowrd(s): {matchingword}\n\n'
                                                          f'Title: {rawtitle}\n\nLink: {link}')
            print(f"* Match Found! Sent a PM! ({rawtitle})")
        else:
            pass


print(f"Successfully logged in as: {reddit.user.me()}\n----------------------------------------------------")
time.sleep(5)
print("Bot is now running!")
time.sleep(1)

while True:
    # ------- Write down the subreddits you want to track using the bot ---------------
    # E.g. i want to track r/askreddit and r/pics:
    #    scansub("askreddit")
    #    scansub("pics")

    scansub("hardwareswap")
    scansub("buildapcsales")
