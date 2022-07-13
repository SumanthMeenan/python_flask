from flask import Flask, render_template
from newsapi import NewsApiClient            #pip install newsapi-python

app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='c2790560e1da4eab982e6467aa6d060d') #instead of using 

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='corona',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')

data = top_headlines["articles"]

for dictionary in data:
    dictionary['title']

news = [val['title'] for val in data]

# news = []
# for val in data:
#     news.append(val['title'])

# /v2/sources
sources = newsapi.get_sources()

@app.route('/home/') #homepage
def home():
    return render_template('index.html', news = news)


if __name__ == "__main__":
    app.run()



# d = {'apple':29, 'mango':32, 'banana':45}
# for item in d:
#     print(item)


# l = [{'apple':29, 'mango':32, 'banana':45}, {'apple':29, 'mango':32, 'banana':45}]
# for item in d:
#     print(item)