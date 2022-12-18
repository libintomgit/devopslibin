# From the newapi.org read the new 
# using the from win32com.client import Dispatch (pip install pywin32 or related module for linux)
# then use it to read the fetched news

import os
import requests
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='a7976eed4a1a42448363ef69cb7f018a')
# api_key = "a7976eed4a1a42448363ef69cb7f018a"
# article_tesla = f'https://newsapi.org/v2/everything?q=tesla&from=2022-11-17&sortBy=publishedAt&apiKey={api_key}'

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')
print(top_headlines)
def speak(str, nothing):
    if str == "Hello":
        os.system(f"say '{str}' &")
        print("did you like it")
    else:
        os.system(f"say '{nothing}'")



if __name__ == '__main__':
    # tesla = requests.get(article_tesla)
    # print(tesla)
    speak("Hello", "nothing to read")

ucimk repository
