<br />
<p align="center">

  <h3 align="center">Web Scraping and Automation </h3>

  <p align="center">
    project_description
    <br />
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites using the Hypertext Transfer Protocol or a web browser.
In this project, I provide implementation and documentation of the projects I did using <a href="#BS">Beautiful Soup</a>, and  <a href="#scrapy">Scrapy</a>, also application using <a href="#BS">Selenium</a> in web scraping and tasks automation.

   <br />
    <br />
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Projects</h2></summary>
  <ol>
    <ul>
            <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/scraping%20empire%20best%20100%20movies%20list">Musical Time Machine (scraping Billboard top 100 list and creating spotify playlist)</a></li>
            <details><br /> Musical Time Machine: Scraping the top 100 list of songs of a given date form the <a href="https://www.billboard.com/charts/hot-100/"> Billboard hot 100 list</a> and using the <a href="https://developer.spotify.com/documentation/web-api/">spotify API</a>  to connect to spotify and create a playlist with the top 100 songs  and return a link to this spotify list</details>
                <ul> - Used modules: <em> requests</em>, <em> bs4</em>, <em>spotipy</em></ul>
    </ul> <br/> 
<ul>
            <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/scraping%20empire%20best%20100%20movies%20list">Scraping Best 100 movies list(empire website)</a></li>
            <details><br /> A project to scrap a live website, <a href="https://www.empireonline.com/movies/features/best-movies-2/">empire online</a>. Getting the Empire's list of the best 100 movies of all time – as voted by readers. and printing the list of the 100 movies  containing the order and the title of each movie</details>
                <ul> - Used modules: <em> requests</em>, <em> bs4</em>, <em>re</em></ul>
    </ul> <br/>
    <ul>
            <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/hacker%20hacker%20news">Scraping Hacker news (ycombinator website)</a></li>
            <details><br /> A project to scrap a live website, <a href="https://news.ycombinator.com/news">ycombinator website</a>, to get the titles and links of the  posted news stories on the website , and the trending stories with the most upvote.</details>
                <ul> - Used modules: <em> requests</em>, <em> bs4</em></ul>
    </ul> <br/>
    <ul>
            <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/scraping%20wikipedia%20article">Scraping Wikipedia Article</a></li>
            <details><br /> A project using the basics of Beautiful soup to scrap the content of a wikipedia article form the local file or using a get request with the link to the live article.<br>
    The local file is compressed just for simplicity and can be extracted to view the content or work with the file, otherwise a get request to the article link will also work.</details>
                <ul> - Used modules: <em> requests</em>, <em> bs4</em> </ul>
    </ul>

  </ol>
</details>

[comment]: <> (<!-- ABOUT THE PROJECT -->)
## About The Project
These projects were developed, documented and tested to improve one's skills  mainly in the following programming languages, and frameworks
* [Python](https://www.python.org/)
* [Beautiful soup ](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://docs.python-requests.org/en/master/)



[comment]: <> (<!-- GETTING STARTED -->)
## Installation 
Install the following modules 
* `bs4 ` 
* `smtplib` 
* `requests` 
* `re`
* `spotipy`

## Example of a get request to and parsing the response with `BeautifulSoup` 
```py
import requests
from bs4 import BeautifulSoup
# initialize a get request to the given url and save the text in a variable response_text
URL = '' # any url 
response_text=requests.get(URL).text
# parse the response_text using BeautifulSoup and the html parser 
soup = BeautifulSoup(response_text, 'html.parser')
# get hold of all anchor tags
anchor_tags= soup.find_all(name="a")
href_links=[]
for tag in anchor_tags:
    # print all the texts in the anchor tags
    print(tag.get_text())
    # adding the href link of the tag to the href_links list 
    href_links.append(tag.get("href"))
    
# Examples of getting elements by their attributes:
heading= soup.find(name="h1", id="name")
heading_text= heading.getText()
print(heading_text)
#getting hold of the tag
heading_text= heading.name
print(heading_text)
#getting hold of the value of an attribute
heading_text= heading.get("class")
print(heading_text)

# Using CSS selectors 
# getting the content of the first anchor tag element in the first paragraph
first_url= soup.select_one( selector="p a")
# getting an element with a given id
name=soup.select_one( selector="name")
print(name.getText())
# getting elements using a class name 
headings=soup.select( selector=".headings")
```