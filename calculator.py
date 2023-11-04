# Splits a string of text into individual words
def textToWords(review): 
    wordList = review.split()
    return wordList

# Removes all puncuation from words and removes filler words from a preset list
def stripWordList(wordList, wordsToRemove): 
    cleanWords = []
    
    # Assemble each word and only include alphanumeric characters
    for word in wordList: 
        wordString = ""
        for char in word: 
            if char.isalnum(): 
                wordString += char.lower()
        
        # Remove empty words, words that are only numbers, and words in the filler list. 
        if wordString != "" and wordString.isalpha() and not wordString in wordsToRemove: 
            cleanWords.append(wordString)
            
    return cleanWords  

# Pull the list of filler words from the file. 
def getWordsToRemove(title): 
    try: 
        wordsFile = open("wordsToRemove.txt", 'r')
    except Exception:
        print("Unable to open words list. Aborting.")
        input('Press ENTER to exit')
        exit(1)
    else: 
        wordsToRemove = wordsFile.readlines()
        for word in range(len(wordsToRemove)): 
            wordsToRemove[word] = wordsToRemove[word][:-1]
        
        # The words in the title of the film are also added to the list
        titleWords = textToWords(title)
        titleWords = stripWordList(titleWords, wordsToRemove)
        wordsToRemove += titleWords
        
    finally: 
        wordsFile.close()
        return wordsToRemove


# Given a list of reviews, convert it into a list of words excluding filler
def createWordList(reviews, wordsToRemove): 
    finalWordList = []
    
    for review in reviews: 
        currentWordList = textToWords(review)
        currentWordList = stripWordList(currentWordList, wordsToRemove)
        finalWordList += currentWordList
    
    return finalWordList

