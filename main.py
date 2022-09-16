import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
access = requests.get(url= URL).content
number = []
movie_title = []
tit = ''
soup = BeautifulSoup(access, 'html.parser')

title = soup.find_all(name='h3', class_='title')
for i in title:
    desc = i.text.split(maxsplit=1)
    number.append(desc[0])
    movie_title.append(desc[1])

number.reverse()
movie_title.reverse()

for i in range(len(number)):
    with open('movies.txt','a') as movie:
        movie.write(f"{number[i]} {movie_title[i]}\n")
