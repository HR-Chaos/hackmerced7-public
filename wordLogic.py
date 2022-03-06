import random
import time
from typing import Dict

#--------------------------------------------------------------------------------------------------#
'''
keyGenerator() - Generates a key of different characters provided a length

@Param length: the requested length of the key

@Return : -1 - if the length parameter is less than 3 or larger than 26
@Return : key - the key created
'''
def keyGenerator(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if ((length > 26) or (length < 3)):
        return -1
    key = ""
    for i in range(length):
        letter = random.choice(alphabet)
        while(letter in key):
            letter = random.choice(alphabet)
        key += letter
    return key

'''
check() - This method checks to see if a word can be made with the characters contained within
          a key

@Param key : the characters that a word can be made out of
@Param word : the word to be checked

@Return : True - if the word can be made with the characters in a key
@Return : False - if the word cannot be made with the characters in a key
@Return : False - if the size of the word is less than 3
'''
def check(key, word):
    if (len(word) < 3):
        return False
    
    temp = ""
    for let in word:
        if let not in temp:
            temp += let

    for let in temp:
        if let not in key:
            return False
    
    return True

'''
dictionarySplit() - This method takes a text file (dictionary) and gets the line where each
                    new "chapter" for a letter is located.

@Param fileName : the name of the file to be read

@Return : listIn - The list containing the lines where each "chapter" for the letter starts
'''
def dictionarySplit(fileName):
    counter = 0
    letter = 'a'
    listIn = []
    listIn.append(0)
    with open(fileName, encoding='utf-8') as infile:
        for line in infile:
            if (line[0] != letter):
                letter = chr(ord(letter) + 1)
                listIn.append(counter)
            counter += 1
    listIn.append(counter)
    return listIn

'''
findWord() - This method checks to see if a word is in a given textfile and range

@Param fileName : the name of the file to be read
@Param word : the word to be looked for
@Param start : the start line within the text file
@Param end : the end line within the text file

@Return : True - if the word is found within the textfile lines specified
@Return : False - if the word is not found within the textfile lines specified
'''
def findWord(fileName, word, start, end):
    with open(fileName, encoding='utf-8') as infile:
        for pos, line in enumerate(infile):
            if pos in range(start, end+1):
                if (word == str(line[0:len(line)-1])):
                    return True
    return False

'''
wordScore() - This method gets the score of a word

@Param word : the word to be scored
@Param initialPts : the points a word of base length would be
@Param baseLen : the base lenth of a word

@Return : 0 - if the baseLen is bigger than the length of the word
@Return : point - the score of the word
'''
def wordScore(word, initialPts, baseLen):
    if (len(word) < baseLen):
        return 0
    point = initialPts + len(word) - baseLen
    return point

def findWordM(fileName, word):
    with open(fileName, encoding='utf-8') as infile:
        for line in infile:
            if (word == str(line[0:len(line)-1])):
                return True
    return False
