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
            if doubleLetter(i, guess[i], guess, correct) == True:
                ans += yellow
            else :
                ans += white
        else:
            ans += green
    return ans

def guessIsWord(guess) :
    file = open("wordle-guess.txt")

    for line in file :
        if guess.upper() == line.strip() :
            return True

    return False

def doubleLetter(index, letter, guess, correct):
    guessCount = 0
    correctCount = 0
    greenCount = 0
    
    for i in range(5):
        if correct[i] == letter:
            correctCount += 1
    for i in range(index + 1):
        if guess[i] == letter:
            guessCount += 1

    for i in range(5):
        if correct[i] == guess[i] and guess[i] == letter:
            greenCount += 1

    if guessCount <= (correctCount - greenCount):
        return True

    return False

