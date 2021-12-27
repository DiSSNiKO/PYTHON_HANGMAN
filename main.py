def scuffedIn(searchLocation, target):
    for x in searchLocation.lower():
        if x == target.lower():
            return True
    return False
def charReplace(string, location, char):
    currentlocation = 1
    temparr = []
    for x in string:
        if currentlocation == location:
            temparr += [char]
        else:
            temparr += [x]
        currentlocation+=1
    restr = ""
    for x in temparr:
        restr+=x
    return restr
def inputSingleChar():
    stringLen = 0
    while stringLen != 1:
        stringLen = 0
        Char = input("ur input >")
        for x in Char:
            stringLen += 1
    return Char
def hangedMan():
    winCondition = 0
    Health = 5
    print(f"STARTING HEALTH {Health}")
    wordToGuess = input("Word to guess > ")
    wordToGuess = wordToGuess.lower()
    hint = ""
    for x in wordToGuess:
        if x == " ":
            hint+= " "
        else:
            hint += "-"
    while Health!=0:
        currentChar = inputSingleChar()
        currentChar = currentChar.lower()
        if scuffedIn(wordToGuess,currentChar) == True:
            location = 1
            for x in wordToGuess:
                if x == currentChar:
                    hint = charReplace(hint,location,currentChar)
                location+=1
            print(hint)
            if hint == wordToGuess:
                return print("YOU RE WINNER")
        else:
            Health-=1
            print(f"HEALTH REMAINS -> {Health}")
    return print("LOSE")
hangedMan()





