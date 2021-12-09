#Name: Alejandra Hernandez
#Date:10/26/2020
#Prog: 12.1 and 12.2

import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from textblob import TextBlob
from wordcloud import WordCloud
import re
from nltk.tokenize.treebank import TreebankWordDetokenizer


def main():
    response = requests.get('https://www.python.org')
    soup = BeautifulSoup(response.content,'html.parser')
    #changed html.parser from html5lib due to error

    text = soup.get_text(strip=True)

    #print(text)

    #only letters
    str = re.findall("[a-zA-Z,.]+",text)
    updated_text = (" ".join(str))


    stops = stopwords.words('english')
    #change
    blob = TextBlob(updated_text)#from text
    print(blob)

    #delete stop words
    items = [word for word in blob.words if word not in stops]

    #make str for wordcloud
    newItems = TreebankWordDetokenizer().detokenize(items)
    #print(type(newItems))




    wordcloud = WordCloud(colormap='prism', background_color = 'white')
    wordcloud = wordcloud.generate(newItems)
    wordcloud = wordcloud.to_file('12.1_Output_myImage.png')


    ##############################         ##############################
    ##############################  12.2   ##############################
    ##############################         ##############################
    print("===========================")
    print("The Sentences:")
    print()
    print(blob.sentences)
    print("===========================")
    print("The Words: ")
    print()
    print(blob.words)
    print("===========================")
    print("The Nouns: ")
    print()
    print(blob.noun_phrases)






main()

