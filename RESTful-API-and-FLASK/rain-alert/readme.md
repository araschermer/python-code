<br />
<p align="center">

  <h3 align="center">Rain Alert</h3>

  <p align="center">
    project_description
    <br />
The Rain alert project: To send an SMS message with the weather updates and information about if it is going to rain during the day.   <br />
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
        <li><a href="#automation">Automating the rain alert script</a></li>
      </ul>
    </li>
        <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project handles the API authentication and  scripts automation. In this project , the [open weather map api](https://api.openweathermap.org) is used to obtain the weather information for a location defined by a latitude and longitude.
Also using the [Twilio ](http://twil.io/secure) sms service of the API to send a message using the twilio api to a given number with the weather updates 


### Built in:
* [Python](Python)

### Modules used:
* [requests](https://pypi.org/project/requests/)
* [twilio](https://www.twilio.com/docs/libraries/python)
### APIs used:
* [open weather map ](https://api.openweathermap.org/data/2.5/onecall)



<!-- GETTING STARTED -->
#Getting Started

To get a local copy up and running follow these simple steps.

### Installation
1-download the project file.\
2-install and import the `requests` module and the `twilio.rest` module.\
3- get a private `API_KEY` from [openweathermap](openweathermap.org)  and save it in the environment variables.\
4- get a `TWILIO_VERIFIED_RECEIVER_NUMBER`, `TWILIO_SENDER_NUMBER`, `account_sid` and `auth_token` from [twilio](twilio.com/console) and save them in the environment variables .\
5- run the `get_weather_details.py` script

### Automation 
This script  can also be automatically executed by as on pythonanywhere service as explained in the comments in the `send_sms_alert.py` script.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

