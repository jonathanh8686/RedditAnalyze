import stats
import matplotlib.pyplot as plt
import college as clg
import praw
from textblob import TextBlob
import json


def saveText(collegeDict):
    txt = {}
    for i in collegeDict:
        if(i not in txt):
            txt[i] = []
        txt[i] = collegeDict[i][1]

    jsn = json.dumps(txt)
    f = open("txtDat.json", "w")
    f.write(jsn)
    f.close()

    print("Text Data saved to file")




print("Start")

colleges = ["ucla", "ucsd", "berkeley", "gatech", "MIT", "brownu", "cmu", "princeton", "harvard", "cornell", "columbia", "dartmouth", "bostonU", "ASU", "caltech", "uiuc",
            "uchicago"]

f = open("config.json", "r")
configData = json.loads(f.read())

print("Process config file")

reddit = praw.Reddit(client_id=configData["client_id"],
                    client_secret=configData["client_secret"],
                    user_agent=configData["user_agent"])

def getFullData(colleges, rdt):
    collegeData = {}

    print("Reddit instance initalized")

    for college in colleges:
        if(college not in collegeData):
            collegeData[college] = []
        collegeData[college] = clg.getCollegeData(college, rdt)

    saveText(collegeData)

    return collegeData

collegeData = getFullData(colleges, reddit)

# --- Running T-Test

clg1Pol = clg.getPolarityData("princeton", reddit)
clg2Pol = clg.getPolarityData("mit", reddit)

# End T-Test

print(stats.ttest(clg1Pol, clg2Pol))

# --- Creating Bar Chart ---
collegePolarity = []
for i in collegeData:
    collegePolarity.append(collegeData[i][0])

fig, ax = plt.subplots()
rect = plt.bar(x=range(len(collegeData)), height=collegePolarity, color =  ["blue"] * 3 + ["red"] + ["blue"] * 16)

ax.set_ylabel('Average Sentiment score vs Colleges')
ax.set_title('Sentiment Score')
plt.xticks(rotation=90)

ax.set_xticks(range(len(collegeData)))
ax.set_xticklabels(collegeData.keys())
plt.show()
# --- End Bar Chart ---

