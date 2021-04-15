<br />
<p align="center">

  <h3 align="center">Stock Trading News Alert</h3>

  <p align="center">
    project_description
    <br />
The Stock Trading News Alert:
To send an SMS message with the stock news and price,and moving direction updates and information.   <br />
    <br />
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project handles the API authentication. In this project , the [news api](https://newsapi.org/v2/everything) is used to obtain the top news about a certain stock.\
The  [alphavantage api  ](https://www.alphavantage.co/query) is used to retrieve information about the stock price changes since the last closing session.\
And the [Twilio ](http://twil.io/secure) sms service of the API  is used to send a message using the twilio api to a given number with the stock price changes and latest news.
##Example:
![Alt text](example.PNG?raw=true "Title")


### Built in:
* [Python](Python)

### Modules used:
* [requests](https://pypi.org/project/requests/)
### APIs used:
* [newsapi](https://newsapi.org/v2/everything)
* [alphavantage ](https://www.alphavantage.co/query)



<!-- GETTING STARTED -->
#Getting Started

To get a local copy up and running follow these simple steps.

### Installation
1-download the project file.\
2-install and import the `requests` module and the `twilio.rest` module.\
3- get a private `STOCK_API_KEY` from [alphavantage](openweathermap.org) and save it in the environment variables.\
4- get a private `NEWS_API_KEY` from the [newsapi](https://newsapi.org) and save it in the environment variables.\
5- get a `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN"`, `TWILIO_SENDER_NUMBER` and `RECEIVER_NUMBER` from [twilio](twilio.com/console) and save them in the environment variables .\
6-define the company_name, stock name and number of messages in main.py script
example:
```py
send_messages(stock="PFE", company_name="Pfizer, Inc.", number_of_messages=1)
```
7- run the `main.py` script

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

