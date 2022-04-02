import random
import linecache

def chooseWord(filename):
    return linecache.getline(filename, random.randint(0, 2314))

def checkCorrect(guess, correct):
    white = '<:white_large_square:959676720930258984>'
    yellow = "<:yellow_square:959677336750534686>"
    green = "<:green_square:959677336750534686>"
    ans = ""

    for i in range(5):
        if guess[i] not in correct:
            ans += white
        elif guess[i] in correct and correct[i] != guess[i]:
            ans += yellow
        else:
            ans += green
    return ans

def geussIsWord(guess) :
    