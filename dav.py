import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
h={'Accept-language': 'en-US'}
f = open('movies.csv', 'w', encoding='utf-8', newline='\n')
file = csv.writer(f)
file.writerow(['Film Description', 'Genre', 'IMDB'])
ind = 1
while ind <6:
    url = "https://srulad.com/movies/page/"+str(ind)
    r = requests.get(url, headers=h)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup= soup.find('div', class_='row')
    all_movies = sub_soup.find_all('div', class_='card movie-item')
    for movie in all_movies:
        description = movie.h2.text
        imdb = movie.span.text
        genre=movie.find('div', class_='card-genre').text
        file.writerow([description, genre, imdb])
        print(imdb)
    ind+=1
    sleep(randint(15,20))

f.close()