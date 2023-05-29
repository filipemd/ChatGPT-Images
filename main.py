from flask import Flask, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def search(query):
    #query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q={query}&source=lnms&tbm=isch'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.find_all('img')
    image_url = images[1]['src']
    return redirect(image_url)

if __name__ == '__main__':
    app.run(debug=True, port="1256")
