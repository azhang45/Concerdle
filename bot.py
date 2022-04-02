from tkinter.tix import MAX
import nextcord
from nextcord.ext import commands
import config
import methods
import linecache
import random

client = commands.Bot(command_prefix="$")
PREFIX = "$"
SOLVED = True
correctWord = ""
NUM_GUESSES = 0
MAX_GUESSES = 6

def checkWin(squares):
    green = "<:green_square:959677336750534686>"
    return squares == green*5




@client.event
async def on_ready():
    print("bot is awake")
    

@client.event
async def on_message(message):
    if message.author.bot:
            return
    
    if (message.author.id == 723910433966260336 or message.author.id == 732979801459261501) and ('print bot version' == message.content.lower() or 'pbv' == message.content.lower()):
            await message.channel.send('2.0.0')

    if message.content[0] == PREFIX:
        global SOLVED
        global correctWord
        global NUM_GUESSES
        global MAX_GUESSES
        if message.content[1:] == 'concerndle' and SOLVED:
            SOLVED = False
            correctWord = methods.chooseWord("wordle-answers-alphabetical.txt")
            await message.channel.send(correctWord)
            return
        elif(not methods.guessIsWord(message.content[1:])):
            await message.channel.send("Invalid guess.")
            return
        elif len(message.content) == 6 and not SOLVED:
            NUM_GUESSES += 1
            await message.channel.send(message.content[1:] + "\n" + methods.checkCorrect(message.content[1:], correctWord)+"\nYou have "+ str(MAX_GUESSES-NUM_GUESSES)+" left.")
            if(checkWin(methods.checkCorrect(message.content[1:], correctWord))):
                await message.channel.send("Congratulations, you got the correct word in "+str(NUM_GUESSES)+" guesses! Are you concerned yet?")
                SOLVED = True
                NUM_GUESSES = 0
            elif(NUM_GUESSES == MAX_GUESSES):
                await message.channel.send("You ran out of guesses. The correct word was `"+correctWord[:-1]+"`. I'm concerned for you.")
                SOLVED = True
                NUM_GUESSES = 0
            return
            

    if message.content == 'test':
        await message.channel.send("<:white_large_square:959676720930258984>" + "<:yellow_square:959677336750534686>" + "<:green_square:959677336750534686>")


# @client.command()
# async def concerndle(ctx):
#     await ctx.send(chooseWord("wordle-answers-alphabetical.txt"))

client.run(config.TOKEN) 