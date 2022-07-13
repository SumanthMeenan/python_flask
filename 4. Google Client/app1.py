from flask import Flask, render_template
from newsapi import NewsApiClient

app1 = Flask(__name__)


# Init
newsapi = NewsApiClient(api_key='c2790560e1da4eab982e6467aa6d060d')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='india',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')

data = top_headlines["articles"]

# news = [val['title'] for val in data]

@app1.route('/home/') #homepage
def home():

    return render_template('index1.html', news = data)


if __name__ == "__main__":
    app1.run()