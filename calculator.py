
def reviewToWords(review): 
    wordList = review.split()
    return wordList

def stripWords(wordList): 
    cleanWords = []
    for word in wordList: 
        wordString = ""
        for char in word: 
            if char.isalnum(): 
                wordString += char
        
        if wordString != "" and wordString.isalpha(): 
            cleanWords.append(wordString.lower())
            
    return cleanWords  

def getWordsToRemove(): 
    try: 
        wordsFile = open("wordsToRemove.txt", 'r')
    except Exception:
        print("Unable to open words list. Aborting.")
        input('Press ENTER to exit')
        exit(1)
    else: 
        wordsToRemove = wordsFile.readlines()
    finally: 
        wordsFile.close()
        return wordsToRemove
        



wordsToRemove = getWordsToRemove()
print(wordsToRemove)

exampleReview = "Overall, the film needed more of the tension the video game series is known for, not to mention their arcade-fun terror, but it still serves as a solid 1987 Five Nights at Freddy’s franchise opener."
words = reviewToWords(exampleReview)
print(stripWords(words))
input('Press ENTER to exit')
