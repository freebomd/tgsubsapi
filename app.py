from flask import Flask,request
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route("/")
def home():
    return "API is working fine"

@app.route('/id',methods=['GET','POST'])
def id():
    w = request.args.get('name')
    base_url = f"https://telegram.dog/{w}"
    r = requests.get(base_url).text
        #print(r)
    soup = bs(r,"html")
        #soup.text
    members_count = soup.find("div",class_="tgme_page_extra").text.replace(" ","").split("members")[0]
        #print(members_count)
    channel_name = soup.find("div", class_="tgme_page_title").text.replace("\n","")
    dp = soup.find("img",class_="tgme_page_photo_image")['src']
    data = {}
    data['status'] = True
    data['name'] = channel_name #Can be used as public group also
    data['image'] = dp
    return data
@app.errorhandler(500)
def page_not_found(e):
    return {'status': False}

if __name__ == "__main__":
    #app.debug = True
    app.run()
