from textblob import TextBlob

def getCollegeData(college, rdt):
    print("Processing " + college)
    submissions = rdt.subreddit(college).new(limit=1000)

    subtext = []
    for sub in submissions:
        if(sub.selftext != ""):
            subtext.append(sub.selftext.strip())

    print("Processed " + str(len(subtext)) + " posts...")

    avgPolarity = 0

    for i in subtext:
        tsn = TextBlob(i)
        avgPolarity += tsn.polarity

    return [avgPolarity / len(subtext), subtext]

def getPolarityData(college, rdt):
    print("Processing " + college)
    submissions = rdt.subreddit(college).new(limit=10000)

    subtext = []
    for sub in submissions:
        if(sub.selftext != ""):
            subtext.append(sub.selftext.strip())

    print("Processed " + str(len(subtext)) + " posts...")

    avgPolarity = 0

    pol = []
    for i in subtext:
        tsn = TextBlob(i)
        pol.append(tsn.polarity)

    return pol


