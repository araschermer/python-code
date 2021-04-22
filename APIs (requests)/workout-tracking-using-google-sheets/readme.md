<br />
<p align="center">

  <h3 align="center">Workout tracker</h3>

  <p align="center">
    project_description
    <br />
The Workout tracker:
To track the workout sessions  with the timing, the exercise type and the amount of calories burnt in the exercise routine.
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
To track the workout sessions  with the timing, the exercise type, and the amount of calories burnt in the exercise routine, given only a sentence, or a few sentences that are processed by a natural language processing model using the [nutritionix track api](https://trackapi.nutritionix.com)
 and stored in a Google sheet though the usage of the [sheety api ](https://api.sheety.co/)
##Example:
![Alt text](example.PNG?raw=true "Title")


### Built With:
* [Python](Python)
* [Google sheets](Google sheets)
### Modules used:
* [requests](https://pypi.org/project/requests/)
### APIs used:
* [nutritionix track api](https://trackapi.nutritionix.com)
* [sheety api ](https://api.sheety.co/)



<!-- GETTING STARTED -->
#Getting Started

To get a local copy up and running follow these simple steps.

### Installation
1-download the project file.\
2-install and import the `requests` module.\
3- get a private `APPLICATION_ID` and `APPLICATION_KEY` from [nutritionix track api](https://trackapi.nutritionix.com) and save them in the environment variables,
 which are required in setting up the API credentials.
```py
# Setup API Credentials
response = requests.get(url=Base_URL, headers=headers)
```
4- get a Bearer Authentication `TOKEN`  and the endpoint of the records sheet (`SHEET_ENDPOINT`) from [sheety](https://api.sheety.co/) and save it in the environment variables .\
\
5- save the private user information, such as `USER_GENDER`, `USER_WEIGHT`, `USER_HEIGHT`,and the `USER_AGE`, in the environment variables.\
######Usage: 
```py
query_params = {
    "query": input("Which exercises did you do today?"),
    "gender": f"{USER_GENDER}",
    "weight_kg": float(USER_WEIGHT),
    "height_cm": int(USER_HEIGHT),
    "age": int(USER_AGE)
}
```
6- run the `main.py` script

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

