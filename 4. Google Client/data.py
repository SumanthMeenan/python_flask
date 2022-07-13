from newsapi import NewsApiClient            #pip install newsapi-python

# Init
newsapi = NewsApiClient(api_key='c2790560e1da4eab982e6467aa6d060d') #instead of using 

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')

print("top_headlines: ", top_headlines['articles'][0]['source'])
