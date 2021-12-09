import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from textblob import TextBlob
from wordcloud import WordCloud
from operator import itemgetter


def main():
    response = requests.get('https://www.python.org')
    response.content
    print("==============================================")

    soup = BeautifulSoup(response.content,'html.parser')
    #changed html.parser from html5lib due to error


    print("==============================================================")
    text = soup.get_text(strip=True)

    print(text)

    print("==========================================================")
    #get rid of stop words

    stops = stopwords.words('english')
    blob = TextBlob(text)
    items = blob.word_counts.items()

    items = [item for item in items if item[0] not in stops]
    items = str(items)

    #sorting by freq
    #sorted_items = sorted(items, key=itemgetter(1), reverse=True)

    #top20 = sorted_items[1:21]
    #myNewWords = top20
    #lol = str(myNewWords)



    wordcloud = WordCloud(colormap='prism', background_color = 'white')
    wordcloud = wordcloud.generate(items)
    wordcloud = wordcloud.to_file('myImage.png')
   # print(items)
    ##############################         ##############################
    ##############################  12.2   ##############################
    ##############################         ##############################
    print("################################################==========================================================")
    print(blob.sentences)
    print("################################################==========================================================")
    print(blob.words)
    print("################################################==========================================================")
    print(blob.noun_phrases)






main()
'''  
    sorted_items = sorted(items, key=itemgetter(1), reverse=True)
    print(sorted_items)
    print("asdasd")
    top20 = sorted_items[1:21]
    myNewWords = top20
    print(myNewWords)

'''
