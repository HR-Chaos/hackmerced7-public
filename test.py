#HackMerced7
#Raivat Alwar

import wordLogic

#--------------------------------------------------------------------#
# Testing:

# Creates the key of size (size)

size = 10
key = wordLogic.keyGenerator(size)
if (key == -1):
    print("The size of the key passed is invalid.")
else:
    print("key: " + key)

    # Checks if word can be made with letters in key and len(word) >= 3
    word = input("Enter word: ")
    applicable = wordLogic.check(key, word)

    if(applicable):
        print(word + " can be made with " + key)
    else:
        print(word + " cannot be made with " + key)

    # creates the list with the chapter lines for the txt file
    dictLines = wordLogic.dictionarySplit("dictionary.txt")

    alphabet = "abcdefghijklmnopqrstubwxyz"
    index = alphabet.index(word[0])
    # checks is word can be found within the dictionary
    print("findWord: ", wordLogic.findWord("dictionary.txt", word, dictLines[index], dictLines[index + 1]))

    # prints the word score
    initial = 10
    baseLen = 4
    print(word, "is worth", wordLogic.wordScore(word, initial, baseLen), "points")

