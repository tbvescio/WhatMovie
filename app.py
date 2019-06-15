from bs4 import BeautifulSoup
import requests
import random
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<categoria>')
def categoria(categoria):

    if categoria == "horror":
        url = "https://www.imdb.com/search/title?genres=horror&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "action":
        url = "https://www.imdb.com/search/title?title_type=feature&num_votes=25000,&genres=action&sort=user_rating,desc"
    elif categoria == "scifi":
        url = "https://www.imdb.com/search/title?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "aventura":
        url = "https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "animacion":
        url = "https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "comedia":
        url = "https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "drama":
        url = "https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "misterio":
        url = "https://www.imdb.com/search/title/?genres=mystery&sort=user_rating,desc&title_type=feature&num_votes=25000,"
    elif categoria == "guerra":
        url = "https://www.imdb.com/search/title/?genres=war&sort=user_rating,desc&title_type=feature&num_votes=25000,"


    if url != 0:

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, features="html.parser")

        x = random.randint(0,49)
        
        #nombre
        llist = soup.find_all('h3',{'class':'lister-item-header'})
        nombre = llist[x].find('a').text
        #rating
        llist = soup.find_all('div',{'class':'inline-block ratings-imdb-rating'})
        rating = llist[x].find('strong').text
        #duracion
        llist = soup.find_all('span',{'class':'runtime'})
        duracion = llist[x].text
        #año
        llist = soup.find_all('span',{'class':'lister-item-year'})   
        anio = llist[x].text         

        nombre += anio

        print(nombre,"\\\\", rating)

        return render_template('result.html', nombre=nombre, rating=rating, duracion=duracion)
    else:   
        abort(404)




if __name__ == "__main__":
    app.run(debug=True)