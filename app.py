from bs4 import BeautifulSoup
import requests
import random
from flask import Flask, render_template

app = Flask(__name__)

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, features="lxml")
llist = soup.find_all('td',{'class':'titleColumn'})


        


@app.route('/')
def index():

    aux = []

    x = random.randint(1,200)

    for i in llist[:x]:  #??
        for j in i.find_all('a'):
            
            print(j.text)
            aux.append(j.text)



    return render_template('index.html', movie=aux[-1])

if __name__ == "__main__":
    app.run(debug=True)