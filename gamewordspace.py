letters = [
    ["h", "o", "l", "i", "d", "a", "y"],
    ["p", "r", "o", "g", "r", "a", "m", "m", "i", "n", "g"],
    ["b", "o", "o", "t", "c", "a", "m", "p"],
    ["f", "l", "o", "w", "c", "h", "a", "r", "t"],
    ["w", "o", "r", "d", "s", "p", "c", "r", "a", "p", "e", "s"],
]
words = [
    {
        "hi",
        "day",
        "dal",
        "hold",
        "lady",
        "hod",
        "lay",
        "lid",
        "hail",
        "load",
        "holy",
        "oil",
    },
    {
        "go",
        "an",
        "in",
        "no",
        "on",
        "map",
        "mom",
        "gap",
        "gag",
        "pig",
        "man",
        "ping",
        "pram",
        "prom",
        "ramp",
    },
    {
        "am",
        "at",
        "to",
        "cab",
        "cap",
        "cob",
        "cop",
        "map",
        "act",
        "bat",
        "camp",
        "comb",
        "boom",
        "pact",
        "atom",
        "boot",
        "tap",
    },
    {
        "of",
        "at",
        "or",
        "to",
        "caw",
        "cow",
        "how",
        "who",
        "calf",
        "flow",
        "flaw",
        "wolf",
        "crow",
        "half",
    },
    {
        "we",
        "do",
        "as",
        "cap",
        "caw",
        "cop",
        "cow",
        "paw",
        "cod",
        "daw",
        "pad",
        "cape",
        "crap",
        "crew",
        "crop",
        "pace",
    },
]
lives = 5
level = 0
score = 0
print("welcome")
name = input("what's your good name?")
print("Game begins...\nBest of luck", name, "!!")
while True:
    print("level=", level + 1)
    print("create 3 words using given letters:")
    print(letters[level])
    wordcount = 0
    match = False
    word = ""
    oldword = ""
    while wordcount == 0 or wordcount < 3:
        match = False
        word = input("Word=")
        word = word.lower()
        if not (word == oldword):
            for w in words[level]:
                if word == w:
                    wordcount += 1
                    score += 1
                    oldword = word
                    match = True
                    break
        elif word == "":
            continue
        if not match:
            print("Oops!! Take another guess...")
            lives -= 1
        if lives <= 0:
            print("Game over!! Better luck next time!!!")
            print("Youre score is=", score)

    wordcount = 0
    match = False
    word = ""
    if lives == 0:
        break
    if level == 4:
        print("Thanks for playing the game!!")
        print("your score is=", score)
        break
    else:
        choice = input("Do you want to continue to next level?(y/n)")
        if choice in "Y,y":
            level += 1
        else:
            print("Thank you for playing the game")
            print("Your score is", score)
