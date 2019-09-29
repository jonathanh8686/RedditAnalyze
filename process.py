import praw
from textblob import TextBlob
import json

print("Started...")

colleges = ["ucla", "ucsd", "berkeley", "gatech", "MIT", "brownu"]
collegeRanking = {}
f = open("config.json", "r")
configData = json.loads(f.read())

print("Process config file")

reddit = praw.Reddit(client_id=configData["client_id"],
                     client_secret=configData["client_secret"],
                     user_agent=configData["user_agent"])

print("Reddit instance initalized")

for college in colleges:
    print("Processing " + college)
    submissions = reddit.subreddit(college).hot(limit=10000)

    print("Submissions gathered.")

    print("Processing Text")
    subtext = []
    for sub in submissions:
        if(sub.selftext != ""):
            subtext.append(sub.selftext.strip())
    print("Processed Text")


    print("Calculating polarity")
    avgPolarity = 0
    for i in subtext:
        tsn = TextBlob(i)
        avgPolarity += tsn.polarity

    collegeRanking[college] = avgPolarity / len(subtext)

print(collegeRanking)
