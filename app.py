from flask import Flask, jsonify, request

import requests, bs4, re

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():

    jsonData = request.get_json()
    keyword = jsonData['keyword']
    urls = jsonData['urls']

    events = list()

    for url in urls:
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        elems = soup.findAll(string=re.compile(keyword))
        
        event = {'url': url, 'count': len(elems)}
        events.append(event)

    return jsonify(events=events)