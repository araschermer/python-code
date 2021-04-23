from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response_text = requests.get(URL).text
soup = BeautifulSoup(response_text, 'html.parser')
# print(soup.prettify())
# in the response we find (by looking up any number between 1 and 100; since the movies are ranked in this way)
# the list mentioned in the <script id="__NEXT_DATA__" type="application/json"> section,
# therefore, we focus our work on analysing this section
data = str(soup.find(id="__NEXT_DATA__").contents[0])  # this section has only one element

# print(data)
titles_indices = []
# here i use pattern matching to find the movies title_index, since the common attribute is
# "titleText":" followed by the movie
# number and name
for title_index in re.finditer(pattern='"titleText":"', string=data):
    titles_indices.append(title_index.start() + len('"titleText":"'))  # starting from the number till the first ","
# before the following attribute
# sort the list from 1 to 100
titles_indices.sort(reverse=True)
best_100_movies = []
for index in titles_indices[:-1]:  # to print the last item once
    end_index = data.find('"', index)
    title = data[index:end_index]
    best_100_movies.append(title)
    print(title)

for movie in best_100_movies:
    with open('best_100_movies.txt', "a") as best_100_movies_file:
        best_100_movies_file.write(f"{movie}\n")
