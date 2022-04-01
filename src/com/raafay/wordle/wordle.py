def run():
    # Get full Wordle List from wordleBank.txt
    with open('C:\Raafay\Coding\Python\Wordle\src\com\\raafay\wordle\wordleBank.txt') as f:
        content = f.readlines()
    wordleList = [x.strip() for x in content]

    # Init Variables
    completed = 0
    word = ""
    hint = ""
    hintValid = True

    wordsArray = []
    hintsArray = []
    greenLetters = []

    # Check how many words have been completed
    while (completed > 5 or completed < 1):
        completed = int(input("How many words have you completed so far?: "))

    for i in range(1, completed + 1):
        while len(word) != 5 or word.lower() not in wordleList:
            word = input("What was Word #%d?: " % (i)).lower()
        print("y = Yellow, g = Green, b = Black. (e.g ygbby)")
        while len(hint) != 5 or not hint.isalpha or not hintValid:
            hint = input("List the hints for Word #%d (y, g, b): " % (i)).lower()
            if hint.isalpha:
                hintValid = True
                for letter in hint:
                    if letter not in "ygb":
                        hintValid = False
                        break
        wordsArray.append(word)
        hintsArray.append(hint)
        word = ""
        hint = ""

    for h in range(completed):
        for i in range(5):
            hint = hintsArray[h][i]
            letter = wordsArray[h][i]
            if hint == "g":
                for wordle in reversed(wordleList):
                    if wordle[i] != letter:
                        wordleList.remove(wordle)
                if letter not in greenLetters:
                    greenLetters.append(letter)
            elif hint == "y":
                for wordle in reversed(wordleList):
                    if letter not in wordle or wordle[i] == letter:
                        wordleList.remove(wordle)
            else:
                for wordle in reversed(wordleList):
                    if letter in wordle and letter not in greenLetters:
                        wordleList.remove(wordle)

    print("Possible Word choices:")
    for wordle in wordleList:
        print(wordle)
    if not wordleList:
        print("None")

while True:
    # main program
    while True:
        run()
        answer = str(input('Run again? (y/n) or Continue? (c): '))
        if answer in ('y', 'n'):
            break

    if answer == 'y':
        continue
    else:
        run()
        break