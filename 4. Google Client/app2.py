from flask import Flask, render_template, request
from newsapi import NewsApiClient

app2 = Flask(__name__)

# Initialized newsapi
newsapi = NewsApiClient(api_key='c2790560e1da4eab982e6467aa6d060d')

@app2.route('/home/') #homepage
def home():
    return render_template('index2.html')

@app2.route('/topic/', methods = ['POST'])
def get_results():
    topic = request.form['topic']
    print("topic: ", topic)
    top_headlines = newsapi.get_top_headlines(q= topic,
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en',
                                          country='in')

    data = top_headlines["articles"]    
    place = top_headlines["country"]

    return render_template('index2.html', news =data, country = place)

if __name__ == "__main__":
    app2.run(debug = True)

#True - development
#False - deployment