<br />
<p align="center">

  <h3 align="center">ISS-Location-Notifier</h3>

  <p align="center">
    project_description
    <br />
A tracker of the International space station position that notifies the user when the ISS if close to the user's given location when it's nighttime 
   <br />
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The International Space Station is a modular space station in low Earth orbit, which is continually circling earth during the day.__
As a part of the 100 days of code challenges, The project is written in python to implement an API to track the international space station(ISS) position and notify the user (via email or sms) when the ISS position is closer to a given latitude and longitude coordinates in the nighttime.
##  Notification email example:
 subject="Look up"
 message="THE INTERNATIONAL SPACE STATION is above you!"

### Built With
* [Python](Python)
## APIs used:
*[sunrise-sunset.org](https://api.sunrise-sunset.org/json)
*[open-notify.org](http://api.open-notify.org/iss-now.json)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
1-Getting the current longitude and altitude for the user from th [https://www.latlong.net](latlong) website, and save it in the environment variables.__
(or replace the    ```$os.environ['LONGITUDE']``` with a string containing the longitude/latitude)__
2-This API would require an internet connection to check the current sunrise and sunset time for the given location.__
3-Sender( and or receiver) Email address, and the password for this email, to enable the automated email notifier,
both email and password should be saved in the environment variables( or replace the environment  variables as in step 1).__
4-SMTP for the email if it is not a yahoo, hotmail or gmail email address.

### Installation

1. Get the code from the project's file
   ```sh
   [ISS-API](https://github.com/amgad01/python-code/tree/main/100%20days%20of%20code/APIs%20(requests)/International-space-station-notifier-API)
   ```
2. Install requests module
   ```sh
   $ python -m pip install requests
   ```
2. import the following modules:
```sh
requests
datetime
time
smtb
```
   
import requests
from datetime import datetime
import smtplib
import time



<!-- USAGE EXAMPLES -->
## Usage
Once you run the script, it will keep  iterating and checking the current location of the ISS and the provided longitude and latitude every minute and once it is close enough it will send the notifying email and stops.




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

