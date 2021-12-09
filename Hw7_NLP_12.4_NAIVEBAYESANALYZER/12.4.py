#Name: Alejandra Hernandez
#Date:10/26/2020
#Prog: 12.4 NAIVEBAYESANALYZER

import requests
from bs4 import BeautifulSoup
#from nltk.corpus import stopwords
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def main():
    response = requests.get('https://local.theonion.com/man-feels-like-girlfriend-hasn-t-been-putting-effort-in-1845439599')
    soup = BeautifulSoup(response.content, 'html.parser')
    myText = soup.find('p')
    #print(myText)
    print("===================================================")
    text = myText.get_text(strip=True)
    print(text)
    print()

    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    print(blob.sentiment)
    print("===================================================")

    #eachSentence = blob.sentences

    for sentence in blob.sentences:
        print(sentence.sentiment)

    #for i in eachSentence:
        #eachSentence.sentiment
    #print(text)
main()