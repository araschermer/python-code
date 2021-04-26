<br />
<p >

<h3 align="center">Scrapy-Practice </h3>

  <p >
    project_description
    <br />
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites using the Hypertext Transfer Protocol or a web browser.
In this project, I provide implementation and documentation of the projects  using <a href="https://scrapy.org/">Scrapy</a> in web scraping.<br/>
Scrapy is a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general-purpose web crawler. 


   <br />
    <br />
  </p>

<!-- TABLE OF CONTENTS -->
<summary><h2 style="display: inline-block">Projects</h2></summary>
      <summary><h2 style="display: inline-block">Projects Using Scrapy</h2></summary>
        <ol>

<ul><li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/scrapy-practice/quotes_scraper">Quotes Scraper Bot </a></li>
<details>In this project, i use scrapy framework to scrape data off <a href="https://quotes.toscrape.com"> quotes to scrape website </a>  and getting the quotes, the  author of the quote and the tags attached to the quotes, with the added functionality to get the spider crawling  and scraping the next pages of the website that hold quotes.Also to save them in database using <a href="sqlite">SQLite</a> and <a href="mysql">Mysql</a> <br /></details>
            <ul> - Used modules: <em>selenium</em>, <em>sqlite3 </em></ul> <br />
            <ul> - open the terminal in the project file <code>quotes_scraper</code> and type<code> scrapy crawl quotes_scraper</code> for the spider to run!.</ul> 
</ul><br/>

<ul><li><a href="https://github.com/amgad01/python-code/tree/main/Web%20scraping%20and%20automation/scrapy-practice/amazon_best_seller_books">Amazon Bestseller Books Bot </a></li>
<details>In this project, i use scrapy framework to scrape data off the amazon best seller books webpage and return the titles,authors and prices of the books on the list 
<br /></details>
            <ul> - Used modules: <em>selenium</em></ul> <br />
            <ul> - open the terminal in the project file <code>amazon_best_seller_books</code> and type<code> scrapy crawl amazon_best_seller_books</code>to run the spider.</ul> 
</ul><br/>


</ol>


<!---[comment]: <> ABOUT THE PROJECT -->

## About The Project

These projects were developed, documented and tested to improve one's skills mainly in the following programming
languages, and frameworks

* [Python](https://www.python.org/)
* [Scrapy](https://scrapy.org/)

[comment]: <> (<!-- GETTING STARTED -->)

## Installation

Install the following modules
* `scrapy`
### To install scrapy 
```shell
pip install Scrapy
```
### To install a project using  `scrapy `
```sh
scrapy startproject project_name
```
### To run a spider / Scrapy crawler
```sh
scrapy crawl spider_name
```
### To run a spider / Scrapy crawler and save the output in a file
```sh
scrapy crawl spider_name -o file_name.extension
```
###### Example
```sh
scrapy crawl quotes_scraper -o quotes_data.csv
```