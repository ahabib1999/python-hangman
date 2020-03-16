def Main():
    RandomWord = GetWord()
    print(RandomWord)
    RandomLetter = GetLetter(RandomWord)
    GuessWord(RandomWord, RandomLetter)
    
def GetWord():
    WordsList = []
    LetterList = []
    
    HangmanWords = open('words.txt', 'r')

    word = HangmanWords.readline()
    word = word.rstrip('\n')

    while word:
        WordsList.append(word)
        word = HangmanWords.readline()
        word = word.rstrip('\n')

    import random
    RandomWord = random.choice(WordsList)
    return RandomWord

def GetLetter(RandomWord): 
    import random
    RandomLetterIndex = random.randint(0, len(RandomWord)- 1)
    RandomLetter = RandomWord[RandomLetterIndex]
    return RandomLetter

def GuessWord(RandomWord, RandomLetter):
    ResultString = ''
    UpdatedDashString = ''
    DashString = '_ '
    score = 0
    guessed = set([RandomLetter])
    ResultList = []

    for num in range(len(RandomWord)):
        if RandomWord[num] == RandomLetter:
            UpdatedDashString += RandomLetter
        else:
            UpdatedDashString += DashString
    print(UpdatedDashString)
    
    UserInput = GetInput()
    ResultList = UpdatedDashString.split(' ')
    if UserInput in guessed:
        print("Incorrect entry")
    else:
        for num in range(len(RandomWord)):
            if RandomWord[num] == UserInput:
                ResultList[num] = UserInput
                score += 1 
                guessed.add(UserInput)
        print(ResultList)
    
        ResultString = " ".join(ResultList)
        print(ResultString)
        print(guessed)
            
def GetInput():
    print('')
    UserInput = input('Please enter a letter from "a" to "z": ')
    return UserInput

Main()




    
    



