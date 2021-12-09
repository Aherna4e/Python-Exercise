#Name: Alejandra Hernandez
#Date:10/26/2020
#Prog: 12.5

from textblob import TextBlob
from textblob import Word
import re
from spellchecker import SpellChecker
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import brown
def main():
       text = open('C:\\Users\\ahern\\OneDrive\\Desktop\\PythonOnline\\Workspace\\hw7_NLP_12.5_SpellCheck\\book.txt', encoding="utf8")
       text = text.read()
       #blob = TextBlob(text)
       #wordBlob = blob.words
       #print(wordBlob)
       str = re.findall("[a-zA-Z,.]+",text) 
       updated_text = (" ".join(str)) 
       print(updated_text) #text without nums
       spell = SpellChecker()

       misspelled = spell.unknown(str) #all words
       #uhhhh
       
       misspelled = TreebankWordDetokenizer().detokenize(misspelled)
       blob = TextBlob(misspelled)
       wordBlob = blob.words

       ######)
       #word_list = brown.words()
       #word_set = set(word_list)
       for i in range(len(wordBlob)):
           new = Word(wordBlob[i])
           print("Orig: ",new,"                Possible Corrections:          ",new.spellcheck())


       #wordBlob = blob.words



main()