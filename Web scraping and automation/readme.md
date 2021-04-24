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
<!---[comment]: <> (Projects Using Beautiful Soup&#41;)--->
    <details open="open">
      <summary><h2 style="display: inline-block">Projects Using Beautiful Soup</h2></summary>
      <ol>
        <ul>
                <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/scraping%20empire%20best%20100%20movies%20list">Musical Time Machine (scraping Billboard top 100 list and creating spotify playlist)</a></li>
                <details><br /> Musical Time Machine: Scraping the top 100 list of songs of a given date form the <a href="https://www.billboard.com/charts/hot-100/"> Billboard hot 100 list</a> and using the <a href="https://developer.spotify.com/documentation/web-api/">spotify API</a>  to connect to spotify and create a playlist with the top 100 songs  and return a link to this spotify list</details>
                    <ul> - Used modules: <em> requests</em>, <em> bs4</em>, <em>spotipy</em></ul>
        </ul> <br/> 
    <ul>
                <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/web%20scraping%20(beautiful%20soup)/amazon-price-tracker">Amazon Proce Tracker</a></li>
                <details><br /> A project to scrap a live website.<br> Given url to a product on  <a href="https://www.amazon.com">Amazon website</a>, This project is to track the current price of the product and send a notification email with with the price update to the given email once the price goes below a given minimum price </details>
                    <ul> - Used modules: <em> requests</em>, <em> bs4</em>, <em>smtplib</em></ul>
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

[comment]: <> (Project Using Beautiful Soup and Selenium)
 <details open="open">
      <summary><h2 style="display: inline-block">Projects Using Beautiful Soup and Selenium</h2></summary>
      <ol>
        <ul>
                <li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/data-entry%20automation(beautiful%20soup%20and%20selenium)">Data-Entry Automation</a></li>
                <details><br /> In this project, I used <a >Selenium</a> and <a>Beautiful Soup</a>  to implement an automate a tool that gets all apartments listings form 
 the <a href="https://www.zillow.com">Zillow</a> website and all important information related to the listings and eventually use the obtained information to fill out a Google form.

I used Beautiful Soup to get:
- Addresses of the properties    
-  Prices of the properties
- Links to the ads on the website
I also used Selenium to fill out a Google Form with all the information that was obtained from the previous step
</details>
                    <ul> - Used modules: <em> requests</em>, <em> bs4</em>, <em>selenium</em></ul>
        </ul> <br/>
    </ol>
    </details>


[comment]: <> (Project Using Selenium)
 <details open="open">
      <summary><h2 style="display: inline-block">Projects Using Selenium</h2></summary>
      <ol>
        <ul><li><a href="https://github.com/amgad01/python-code/blob/main/Web%20scraping%20and%20automation/Automation%20(Selenium)/upcoming-events(python.org).py">Upcoming events (python.org
)</a></li>
                <details><br /> In this project, I use <a >Selenium</a> to automate  the chrome browser to get to the <a>python.org</a> website and get the upcoming events listed in the main page.</details>

<ul> - Used modules: <em>selenium</em></ul> 
- to run the project: save the local path to the <code>chromedriver.exe</code> file in the environment variable under the name <code>"CHROME_DRIVER"</code>  and run the <code>upcoming-events(python.org).py </code> file. </ul> <br/>
    </ol>
    </details>

<ol>
        <ul><li><a href="https://github.com/amgad01/python-code/blob/main/Web%20scraping%20and%20automation/Automation%20(Selenium)/LAB%20Report%20Signup.py">LAB-REPORT signup</a></li>
                <details><br /> In this project, I implement simple <a >Selenium</a>  functionality to in order to automate the chrome browser to fill out a form and click submit on a given webpage.</details>

<ul> - Used modules: <em>selenium</em>, <em>selenium.webdriver.common.keys</em></ul> 
- to run the project: save the local path to the <code>chromedriver.exe</code> file in the environment variable under the name <code>"CHROME_DRIVER"</code>  and run the <code>LAB Report Signup.py</code> file. </ul> <br/>
    </ol>
  </ol>
</details>

[comment]: <> (<!-- ABOUT THE PROJECT -->)
## About The Project
These projects were developed, documented and tested to improve one's skills  mainly in the following programming languages, and frameworks
* [Python](https://www.python.org/)
* [Beautiful soup ](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://docs.python-requests.org/en/master/)
* [Selenium](https://www.selenium.dev/)


[comment]: <> (<!-- GETTING STARTED -->)
## Installation 
Install the following modules 
* `bs4 ` 
* `selenium` 
* `smtplib` 
* `requests` 
* `re`
* `spotipy`

## Example of a get request and parsing the response with `BeautifulSoup` 
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

## Example from the `cookie-clicker bot` project: Creating a driver using selenium  
```py
import os
from selenium import webdriver
# In order to use Google chrome 
# get the CHROME_DRIVER path saved in the environment variables, 
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(CHROME_DRIVER)
# get the driver to open a given link 
driver.get("https://orteil.dashnet.org/experiments/cookie/")
# Get cookie
cookie = driver.find_element_by_id("cookie")
# Get upgrade-items ids.
items = driver.find_elements_by_css_selector("#store div")
print(f"items={items}")
item_ids = [item.get_attribute("id") for item in items]
print(f"item_ids={item_ids}")
``` 
