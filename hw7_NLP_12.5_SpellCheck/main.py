#Name: Alejandra Hernandez
#Date:10/26/2020
#Prog: 12.5


from textblob import TextBlob
from spellchecker import SpellChecker
from textblob import Word
from nltk.corpus import brown
import re


def main():
    text = open('C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\hw7_NLP_12.5_SpellCheck\\book.txt',
                encoding="utf8")
    text = text.read()
    blob = TextBlob(text)
    # print(blob)
    word_list = brown.words()
    word_set = set(word_list)

    wordBlob = blob.words
    print(wordBlob)
    for i in range(len(wordBlob)):
        new = Word(wordBlob[i])
        if wordBlob[i] in word_set == False:
            print("Possible Corrections: ", new.spellcheck())


'''
   print("===============================================")
   for i in range(len(wordBlob)):
      new = Word(wordBlob[i])
      print(new.spellcheck())


   #for word in wordBlob:
      #print(wordBlob[word].spellcheck())
   #checkText = Word(wordBlob)
   # #print(checkText.spellcheck())

'''

main()
